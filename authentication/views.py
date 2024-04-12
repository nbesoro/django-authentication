from django.shortcuts import render, redirect
from django.contrib.auth import logout


def index(request):
    return render(request, "index.html")


def register_view(request):
    return render(request, "register.html")


def login_view(request):
    return render(request, "login.html")


# logout page
def logout_view(request):
    logout(request)
    return redirect("login")
