from django.shortcuts import render,redirect,get_object_or_404
from base.models import ToDo
from base.forms import ToDoForm
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    todos = ToDo.objects.all()
    context =  {'todos': todos}
    return render(request, 'base/home.html', context)

def create(request):
    form = ToDoForm(request.POST)
    if request.method == 'POST':
        form = ToDoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'credentials not valid')
    context = {'form':form}
    return render(request, 'base/create.html',  context)

def read_or_details(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    context = {'todo': todo}
    return render(request, 'base/details.html', context)

def update(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    form = ToDoForm(instance=todo)
    if request.method == 'POST':
        form = ToDoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('details', pk=pk)
        else:
            messages.error(request, 'credentials not valid')
    context = {'form': form, 'todo': todo}
    return render(request, 'base/update.html', context)

def delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    context = {'todo':todo}
    return render(request, 'base/delete.html', context)

        

