from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm,ChangeUserPassword


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You have been log in successfully")
            return redirect("home")

        else:
            messages.error(request, "You have entered wrong credentials, please try again")
            return redirect("authenticate:login")

    else:
        return render(request, "authenticate/login.html", {})


def logout_user(request):
    logout(request)
    messages.error(request, "You have logout successfully")
    return render(request, "authenticate/logout.html")


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user creation is successful and user verification for login is under steps
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,"You Have Registered Successfully"    )
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register.html', {'form': form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # user creation is successful and user verification for login is under steps
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,"You Have Registered Successfully"    )
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'authenticate/edit_profile.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = ChangeUserPassword(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # user creation is successful and user verification for login is under steps
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request,"You Have Registered Successfully")
            return redirect('home')
    else:
        form = ChangeUserPassword(user=request.user)
    return render(request, 'authenticate/change_password.html', {'form': form})

