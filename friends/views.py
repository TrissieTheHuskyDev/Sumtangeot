from django.shortcuts import render
from .models import Friend

# Create your views here.

def index(request):
    friend_list = Friend.objects.all()
    return render(request, 'index.html', {'friend_list':friend_list})