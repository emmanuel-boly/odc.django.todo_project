from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {'todos': todos, 'form': form}
    return render(request, 'todo_app/todo_list.html', context)

def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {'form': form}
    return render(request, 'todo_app/todo_update.html', context)

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')

    context = {'todo': todo}
    return render(request, 'todo_app/todo_delete.html', context)
