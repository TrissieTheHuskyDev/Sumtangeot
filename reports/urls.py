from django.urls import path
from . import views

urlpatterns = [
    path('', views.report, name='report'),
    path('manage/', views.report_manage),
    path('manage/<int:pk>/', views.report_manage_detail),
    path('fileupload/', views.FileFieldView.as_view())
]