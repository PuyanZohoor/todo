from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm

# Create your views here.
def add(request):
    context = {}
    if request.method == 'POST':
        task = Task(title = request.POST['title'], done = request.POST['done'])
        task.save()
    tasks = Task.objects.all()
    context = {'tasks': tasks}
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
    if request.method == 'POST':
        Task.objects.filter(id=id).delete() 
    tasks = Task.objects.all()
    context = {'tasks': tasks}    
    return render(request, 'index.html', context=context)

def list(request):
    context = {}
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {'tasks': tasks}
    return render(request, 'index.html', context=context)

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
                return redirect(request, 'index.html')
            else:
                message = 'Login failed!'
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)

def logout_part(request):
    logout(request)
    return redirect(request, 'login_page.html')
