from django.shortcuts import render, redirect
from django.http import HttpResponse as res
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


@login_required(login_url='/login')
def home(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "base/home.html", context)


def login_user(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            print("you cannot login ")
        users = authenticate(username=user.username, password=password)
        if users is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'base/login.html')


def log_out(request):
    logout(request)
    return redirect('/login')


def signup(request):

    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get('username')
        password1 = request.POST.get("password1")
        password2 = request.POST.get('password2')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        user.save()
        return redirect('home')
    return render(request, "base/signup.html")


def logout(request):
    pass


def reset(request):
    pass


def token(request):
    pass
