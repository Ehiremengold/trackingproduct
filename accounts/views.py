from django.shortcuts import render
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from .forms import RegistrationForm, AccountAuthenticationForm
from django.contrib import messages
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import User, auth

# Create your views here.


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))
    return redirect


def register(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {user.email}")
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('login')
        else:
            context['registration_form'] = form
    return render(request, 'register.html', context)




def login(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    destination = get_redirect_if_exists(request)
    if request.method == "POST":
        form = AccountAuthenticationForm(request.POST or None)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('/')
        else:
            context['login_form'] = form
    return render(request, 'login.html', context)



def logout(request):
    logout(request)
    return redirect('/')





