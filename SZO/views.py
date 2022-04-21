from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(response):
    return render(response, "SZO/home.html", {})


def login(response):
    return render(response, "SZO/login.html", {})
