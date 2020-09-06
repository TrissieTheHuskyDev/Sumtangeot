from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a/', views.a, name='a'),
    path('sum/', views.sum, name='sum'),
    path('donation/', views.donation, name='donation'),
    path('animal/', views.animal, name='animal'),
]
