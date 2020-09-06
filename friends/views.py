from django.shortcuts import render, get_object_or_404
from .models import Friend
from columns.models import Column

# Create your views here.

def index(request):
    friend_list = Friend.objects.all()
    column_list = Column.objects.all()
    return render(request, 'index.html', {'friend_list':friend_list, 'column_list':column_list})

def detail(request, friend_id):
    friend = get_object_or_404(Friend, pk=friend_id)
    return render(request, 'detail.html', {'friend':friend})

def sum(request):
    return render(request, 'sum.html')

def donation(request):
    return render(request, 'donation.html')