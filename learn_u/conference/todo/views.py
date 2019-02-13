from django.shortcuts import render
from .models import TodoGroup, Todo
from django.contrib.auth.models import User

def index(request):
        return render(request, 'todo/index.html');

def todo_groups(request):
    print('debug here', request.user)
    todo_group_list = TodoGroup.objects.filter(author=request.user)
    # todo_group_list = TodoGroup.objects.all()
    return render(request, 'todo/todogroups.html', {'todo_group_list': todo_group_list})
