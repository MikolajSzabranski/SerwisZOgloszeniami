from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def home(response):
    return render(response, "SZO/home.html", {})


def offer(response):
    return render(response, "SZO/offer.html", {})


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = UserCreationForm()

    return render(response, "SZO/register.html", {"form": form})


def logout(response):
    logout(response)
    messages.success(response, "You were logged out!")
    return render(response, "SZO/home.html", {})
