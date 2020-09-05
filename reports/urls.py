from django.urls import path
from . import views

urlpatterns = [
    path('', views.report, name='report'),
    path('fileupload/', views.FileFieldView.as_view())
]