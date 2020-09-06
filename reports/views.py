import os, json
from pathlib import Path
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from .models import ReportImage, Report
from .forms import FileFieldForm

def report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        report = Report()
        report.lat = data['latitude']
        report.lng = data['longitude']
        report.reporter = User.objects.get(pk=data['user_id'])
        report.comment = data['comment']
        report.kor_name = data['kor_name']
        report.save()
        for image in data['images']:
            report.images.add(ReportImage.objects.get(pk=image))
    return render(request, 'report.html')

def report_manage(request):
    reports = Report.objects.all()
    return render(request, 'report_manage.html', {'reports': reports})

def report_manage_detail(request, pk):
    detail = get_object_or_404(Report, pk=pk)
    return render(request, 'report_manage_detail.html', {'detail': detail})

class FileFieldView(FormView):
    form_class = FileFieldForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            report_image_id = None
            for f in files:
                with open(Path(str(settings.MEDIA_ROOT) + "/report/" + f.name).resolve(), 'wb+') as destination:
                    img_temp = NamedTemporaryFile()
                    for chunk in f.chunks():
                        img_temp.write(chunk)
                    img_temp.flush()
            
                    report_image = ReportImage()
                    report_image.image.save(
                        f.name,
                        File(img_temp)
                    )
                    report_image.save()
                    report_image_id = report_image.id

                os.remove(Path(str(settings.MEDIA_ROOT) + "/report/" + f.name).resolve())

            return JsonResponse({'form': True, 'report_image_id': report_image_id})
        else:
            return JsonResponse({'form': False})