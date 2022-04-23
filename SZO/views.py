from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def home(response):
    return render(response, "SZO/home.html", {})


def login(response):
    return render(response, "SZO/login.html", {})


def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = UserCreationForm()

    return render(response, "SZO/register.html", {"form": form})
