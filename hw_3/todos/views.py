from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from django.http import JsonResponse

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todos:todo_list')

def api_todo_list(request):
    todos = Todo.objects.all().values()
    return JsonResponse(list(todos), safe=False)

def api_todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return JsonResponse({'title': todo.title, 'description': todo.description, 'due_date': todo.due_date, 'status': todo.status})
