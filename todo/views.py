from django.shortcuts import render
from .models import Task

# Create your views here.
def add(request):
    context = {}
    if request.method == 'POST':
        task = Task(title = request.POST['title'], done = request.POST['done'])
        task.save()
        context = {'task': task}
    return render(request, 'index.html', context=context)


def edit(request, id):
    context = {}
    if request.method == 'POST':
        task = Task.objects.filter(id=id)
        if task is not None:
            task.title = request.POST['title']
            task.done = request.POST['done']
            task.save()
        context = {'task': task}
    return render(request, 'index.html', context=context)

def delete(request, id):
    if request.method == 'DELETE':
        Task.objects.filter(id=id).delete() 
    return render(request, 'index.html')

def list(request):
    context = {}
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {'tasks': tasks}
    return render(request, 'index.html', context)