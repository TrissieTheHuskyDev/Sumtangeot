from django.shortcuts import render, get_object_or_404, redirect
from .forms import ColumnForm, CommentForm
from .models import Column, Comment
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.

def columns_boards(request):
    column_list = Column.objects.all()
    return render(request, 'column_board.html', {'column_list':column_list})

@login_required(login_url='/login/') # django의 decorators
def columns_create(request):
    if request.method == 'POST':
        column_form = ColumnForm(request.POST)
        if column_form.is_valid():
            column_form.save()
            return redirect('/columns/')
    else:
        column_form = ColumnForm()
    return render(request, 'column_create.html', {'column_form':column_form})

def columns_detail(request, column_id):
    column = get_object_or_404(Column, pk=column_id)
    comment_form = CommentForm()
    return render(request, 'column_detail.html', {'column':column, 'comment_form':comment_form})

@login_required(login_url='/login/') # django의 decorators
def columns_update(request, column_id):
    column_update = get_object_or_404(Column, pk=column_id)
    if request.method == 'POST':
        column_form = ColumnForm(request.POST, instance=column_update)
        if column_form.is_valid():
            column_form.save()
            return redirect('/columns/detail/'+str(column_id))
    else:
        column_form = ColumnForm(instance=column_update)
    return render(request, 'column_update.html', {'column_form':column_form})

@login_required(login_url='/login/') # django의 decorators
def columns_delete(request, column_id):
    column = Column.objects.get(pk=column_id)
    column.delete() 
    return redirect('/columns/')

''' Comment '''
@login_required(login_url='/login/') # django의 decorators
def create_comment(request, column_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.column = Column.objects.get(pk=column_id)
        temp_form.save()
        return redirect('columns_detail', column_id)

@login_required(login_url='/login/') # django의 decorators
def delete_comment(request, column_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('columns_detail', column_id)
    else:
        raise PermissionDenied