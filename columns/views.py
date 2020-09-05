from django.shortcuts import render
from .forms import ColumnForm
from .models import Column

# Create your views here.

def create(request):
    form = ColumnForm()
    return render(request, 'column_create.html', {'form':form})

def boards(request):
    return render(request, 'column_board.html')

def update(request, column_id):
    return render(request, 'column_update.html')
