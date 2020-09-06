from django.shortcuts import render, get_object_or_404, redirect
from .forms import ColumnForm
from .models import Column

# Create your views here.

def boards(request):
    column_list = Column.objects.all()
    return render(request, 'column_board.html', {'column_list':column_list})

def create(request):
    if request.method == 'POST':
        column_form = ColumnForm(request.POST)
        if column_form.is_valid():
            column_form.save()
            return redirect('/columns/')
    else:
        column_form = ColumnForm()
    return render(request, 'column_create.html', {'column_form':column_form})

def detail(request, column_id):
    column = get_object_or_404(Column, pk=column_id)
    return render(request, 'column_detail.html', {'column':column})

def update(request, column_id):
    column_update = get_object_or_404(Column, pk=column_id)
    if request.method == 'POST':
        column_form = ColumnForm(request.POST, instance=column_update)
        if column_form.is_valid():
            column_form.save()
            return redirect('detail', column_id)
    else:
        column_form = ColumnForm(instance=column_update)
    return render(request, 'column_update.html', {'column_form':column_form})

def delete(request, column_id):
    column = Column.objects.get(pk=column_id)
    column.delete() 
    return redirect('/columns/')