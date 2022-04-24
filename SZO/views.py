from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, CreateOffer
from .models import CustomUser, JobOffer


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            form = PasswordChangeForm()
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'SZO/home.html', {'form': form})


def offer(response):
    offers = JobOffer.objects.all()
    return render(response, "SZO/offer.html", {"offers": offers})


def addOffer(response):
    if response.method == "POST":
        form = CreateOffer(response.POST)
        if form.is_valid():
            user = response.user
            text = form.cleaned_data['text']
            title = form.cleaned_data['title']
            city = form.cleaned_data['city']
            tel_num = form.cleaned_data['tel_number']
            newOffer = JobOffer(user=user, text=text, title=title, city=city, tel_number=tel_num)
            newOffer.save()
            return redirect("/offer")
    else:
        form = CreateOffer()
    return render(response, "SZO/addOffer.html", {"form": form})


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
    return render(response, "SZO/home.html", {})