from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Column(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    content = RichTextField()