from django.urls import path
from . import views

urlpatterns = [
    path('', views.columns_boards, name='columns_boards'),
    path('create/', views.columns_create, name='columns_create'),
    path('detail/<int:column_id>', views.columns_detail, name='columns_detail'),
    path('update/<int:column_id>', views.columns_update, name='columns_update'),
    path('delete/<int:column_id>', views.columns_delete, name='columns_delete'),
]
