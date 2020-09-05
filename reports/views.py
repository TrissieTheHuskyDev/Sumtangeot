import json
from django.views.generic import CreateView
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ReportImage, Report
from .forms import ReportImageForm
from .response import JSONResponse, response_mimetype

def report(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        report = Report()
        report.lat = data['latitude']
        report.lng = data['longitude']
        report.reporter = User.objects.get(id=data['user_id'])
        report.comment = data['comment']
        report.kor_name = data['kor_name']
        report.save()
    else:
        form = ReportImageForm()
    return render(request, 'report.html', {'form': form})

class PictureCreateView(CreateView):
    model = ReportImage
    fields = ['image']

    def form_valid(self, form):
        self.object = form.save()
        data = {'status': 'success'}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        return response