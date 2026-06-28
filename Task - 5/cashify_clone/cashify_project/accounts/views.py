from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django import forms

def add_bootstrap_classes(form):
    for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'
    return form

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    form = add_bootstrap_classes(form)

    return render(request,
                  'accounts/register.html',
                  {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('device_list')
    else:
        form = AuthenticationForm()

    form = add_bootstrap_classes(form)

    return render(request,
                  'accounts/login.html',
                  {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

