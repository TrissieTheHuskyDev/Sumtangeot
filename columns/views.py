from django.shortcuts import render
from .forms import ColumnForm

# Create your views here.

def create(request):
    form = ColumnForm()
    return render(request, 'column_create.html', {'form':form})

def columns(request):
    return render(request, 'columns.html')