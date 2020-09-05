from django.db import models
from django.contrib.auth.models import User

class ReportImage(models.Model):
    image = models.ImageField(upload_to='', null=True)
    

class Reports(models.Model):
    # 제보 위치
    lat = models.FloatField()
    lng = models.FloatField()
    # 제보 시간
    time = models.DateTimeField(auto_now=True)
    # 제보 당시 사진들
    images = models.ManyToManyField(ReportImage, null=True)
    # 제보자
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)