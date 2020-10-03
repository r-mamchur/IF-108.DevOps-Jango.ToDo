from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from .forms import TodoForm
from .models import ToDo, CFG_States

def home(request):
    todoes = ToDo.objects.order_by('due')

    return render(request, 'home.html', {'todoes': todoes})

def todo_detail(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_new(request):
    if request.method == "POST":
#        todo.state = CFG_States.objects.first() #  не 
#        todo.state = TodoForm(initial={'tank': 123})
#        form = TodoForm(request.POST, initial={'todo.state': 1})   he
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.created_at = timezone.now()
#            todo.state = CFG_States.objects.first() #  не до того а після того
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('/')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_edit.html', {'form': form})

def todo_edit2(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_edit.html', {'form': form})

