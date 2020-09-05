from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards, name='boards'),
    path('create/', views.create, name='create'),
    path('detail/<int:column_id>', views.detail, name='detail'),
    path('update/<int:column_id>', views.update, name='update'),
    path('delete/<int:column_id>', views.delete, name='delete'),
]
