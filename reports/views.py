import os, json
from pathlib import Path
from django.views.generic.edit import FormView
from django.shortcuts import render
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
        report = report.save(commit=False)
        print(report)
        report.lat = data['latitude']
        report.lng = data['longitude']
        report.reporter = User.objects.get(pk=data['user_id'])
        report.comment = data['comment']
        report.kor_name = data['kor_name']
        for image in data['images']:
            report.images.add(ReportImage.objects.get(pk=image))
        report.save()
    return render(request, 'report.html')

class FileFieldView(FormView):
    form_class = FileFieldForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            report_images = []
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
                    report_images.append(report_image.id)

                os.remove(Path(str(settings.MEDIA_ROOT) + "/report/" + f.name).resolve())

            return JsonResponse({'form': True, 'images': report_images})
        else:
            return JsonResponse({'form': False})