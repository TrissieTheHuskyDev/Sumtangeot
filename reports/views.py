from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ReportImage, Report
import json

# Create your views here.
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
    return render(request, 'report.html')