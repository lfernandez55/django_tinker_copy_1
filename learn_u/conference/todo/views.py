from django.shortcuts import render
from .models import TodoGroup, Todo
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import NewTodoForm
from django.shortcuts import redirect

def index(request):
        return render(request, 'todo/index.html');

def todo_groups(request):
    print('debug here', request.user)
    todo_group_list = TodoGroup.objects.filter(author=request.user)
    # todo_group_list = TodoGroup.objects.all()
    return render(request, 'todo/todogroups.html', {'todo_group_list': todo_group_list})

def groups_and_todos(request):
    #the fields from the TodoGroup model have to have the todo_group prefix. that prefix is defined
    #in the Todo model.  in addition after the prefix one has to put in two dashes. the filter
    #was added so that only the logged in user's groups and todos would display
    groups_and_todos_list = Todo.objects.all().values('label','finished','todo_group__name').filter(todo_group__author=request.user)
    return render(request, 'todo/groups_and_todos.html', {'groups_and_todos_list': groups_and_todos_list})

def todos_by_group(request,todo_group_id):
    #the hyphen before sequence determines whether to order by ascending or descending
    todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence')
    return render(request, 'todo/todos.html', {'todos': todos, 'todo_group_name': todos[0].todo_group, 'todo_group_id': todo_group_id })

def new_todo(request,todo_group_id):
    todo = get_object_or_404(Todo, pk=1)
    error=""
    if request.method == 'POST':
        label = request.POST['label']
        if 1 > 15:
           error = 'Sample error here'
        else:
           todo = Todo.objects.create(label=label,todo_group_id=todo_group_id)
           return todos_by_group(request,todo_group_id)
        form = NewTodoForm()
        return render(request, 'todo/new_todo.html', {'todo': todo, 'form': form,'error': error, 'todo_group_id': todo_group_id})
        print('debugggg')
    else:
        form = NewTodoForm()
    return render(request, 'todo/new_todo.html', {'todo': todo, 'form': form, 'error': error, 'todo_group_id': todo_group_id })
