from django.db import models

# Create your models here.

class Friend(models.Model):
    # 사용 필드: 분류군, 등급, 국명, 학명, 이미지

    ''' 분류군 목록 '''
    GROUP_CHOICES = (
        ("mammals", "포유류"),
        ("birds", "조류"),
        ("amphibians", "양서파충류"),
        ("fishs", "어류"),
        ("insects", "곤충류"),
        ("invertebrates", "무척추동물"),
    )

    ''' 등급 목록 '''
    LEVEL_CHOICES = (
        ("first", "1급"),
        ("second", "2급"),
        ("third", "3급"),
    )

    group = models.CharField(choices=GROUP_CHOICES, max_length=20)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=10)
    kor_name = models.CharField(max_length=30)
    scientific_name = models.CharField(max_length=100)
    image = models.ImageField(default='static/default/default_logo.png')

    def __str__(self):
        return self.kor_name