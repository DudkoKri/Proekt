from django.shortcuts import render, redirect
from .models import kamni
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def index (request):
    return render(request,'glav/glav.html')

def about (request):
    tasks = kamni.objects.all()
    return render(request,'glav/kamni.html', {'title': 'Виды камней', 'tasks': tasks, 'ss': 'Выбрать'})

def malahit(request):
    return render(request, 'glav/malahit.html')

def agat(request):
    return render(request, 'glav/agat.html')

def bir(request):
    return render(request, 'glav/bir.html')

def yant(request):
    return render(request, 'glav/yant.html')

def avant(request):
    return render(request, 'glav/avant.html')

def reg (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vhod')
    else:
        form = UserCreationForm()
    return render(request,'glav/reg.html', {'form': form,})

def vhod (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('kamni')
    else:
        form = AuthenticationForm()
    return render(request,'glav/vhod.html', {'form': form,})


