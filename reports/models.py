from django.db import models
from django.contrib.auth.models import User

class ReportImage(models.Model):
    image = models.ImageField(upload_to='report')
    

class Report(models.Model):
    # 일반 제보 (필수 정보)
    # 제보 위치
    lat = models.FloatField()
    lng = models.FloatField()
    # 제보 시간
    time = models.DateTimeField(auto_now=True)
    # 제보자
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    # 제보자 설명
    comment = models.TextField()

    # 상세 제보 (선택 정보)
    # 동물 이름
    kor_name = models.CharField(max_length=30)
    # 제보 당시 사진들
    images = models.ManyToManyField(ReportImage, null=True)

    def __str__(self):
        return str(self.pk)