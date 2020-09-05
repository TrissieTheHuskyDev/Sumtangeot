from django.urls import path
from . import views
from .views import PictureCreateView

urlpatterns = [
    path('', views.report, name='report'),
    path('upload', PictureCreateView.as_view(), name='upload_report')
]