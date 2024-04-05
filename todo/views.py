from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Task
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
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo.views.list')
            else:
                return render(request, 'login_page.html', {"error": "Invalid username or password."})
        else:
            print("Form errors:", form.errors)  # Print form errors if any
    else:
        form = LoginForm()
    return render(request, 'login_page.html', {'form': form})




def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            newUser = User.objects.create_user(username, email, password)
            newUser.save()
            return redirect('todo.views.list')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'sign_up.html', context=context)


def logout_part(request):
    logout(request)
    return redirect('todo.views.login_page')
