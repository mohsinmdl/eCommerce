from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
    return render(request, 'home_page.html', {
        'title': 'Home Page',
        'discription': 'lorem ipsum can do anything'
    })


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'home_page.html', {
        'title': 'Contact',
        'discription': 'Please enter your contact information',
        'form': form
    })


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'title': 'Login',
        'discription': 'Please enter your Credentials information',
        'form': form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print("IS user logged in ")
        print(request.user.is_authenticated)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Login Successfjully")
            redirect('/login')
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(request, 'auth/login.html', context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'title': 'Registration',
        'discription': 'Please enter your information',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user =  (username,email,password)
    return render(request, 'auth/register.html', context)
