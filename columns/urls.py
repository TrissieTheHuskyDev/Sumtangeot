from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards, name='boards'),
    path('create/', views.create, name='create'),
    # path('update/<int:>', views.update, name='update'),
]
