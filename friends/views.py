from django.shortcuts import render
from .models import Friend
from columns.models import Column

# Create your views here.

def index(request):
    friend_list = Friend.objects.all()
    column_list = Column.objects.all()
    return render(request, 'index.html', {'friend_list':friend_list, 'column_list':column_list})

def a(request):
    return render(request, 'a.html')

def sum(request):
    return render(request, 'sum.html')

def donation(request):
    return render(request, 'donation.html')

def animal(request):
    friend_list = Friend.objects.all()
    column_list = Column.objects.all()
    return render(request, 'animal.html', {'friend_list':friend_list, 'column_list':column_list})