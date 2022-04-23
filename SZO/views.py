from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser


# Create your views here.

def home(response):
    return render(response, "SZO/home.html", {})


def offer(response):
    return render(response, "SZO/offer.html", {})


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            typeUser = form.cleaned_data['typeUser']
            group = Group.objects.get(name=typeUser)
            group.user_set.add(user)
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


def logout(response):
    logout(response)
    messages.success(response, "You were logged out!")
    return render(response, "SZO/home.html", {})
