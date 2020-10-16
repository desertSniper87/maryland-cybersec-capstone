from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import NewMsgForm
from .models import Message


def index(request):
    msgs = None
    if request.user.is_authenticated:
        msgs = Message.objects.filter(receiver=request.user)
    return render(request, 'messanger/index.html', {'msgs': msgs})

def new_msg(request):
    if request.method == 'POST':
        form = NewMsgForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()

            return redirect('index')
    else:
        form = NewMsgForm()
    return render(request, 'messanger/new_msg.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

