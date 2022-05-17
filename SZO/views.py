from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import RegisterForm, CreateOffer
from .models import JobOffer


# Create your views here.
def home(request):
    offers = JobOffer.objects.all()
    perPage = 3
    p = Paginator(offers, perPage)
    page = request.GET.get('page')
    offersList = p.get_page(page)
    # nums = "a" * offersList.paginator.num_pages
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
        return render(request, 'SZO/home.html',
                      {'form': form,
                       "offers": offers,
                       "offersList": offersList}
                      )


def offer(response):
    perPage = 5
    if response.method == "POST":
        searched = response.POST['searched']
        perPage = response.POST['selectBox']
        offers = JobOffer.objects.filter(title__contains=searched)
    else:
        offers = JobOffer.objects.all()
        searched = False
    p = Paginator(offers, perPage)
    page = response.GET.get('page')
    offersList = p.get_page(page)
    nums = "a" * offersList.paginator.num_pages

    return render(response, "SZO/offer.html",
                  {"offers": offers,
                   "searched": searched,
                   "offersList": offersList,
                   "nums": nums,
                   "perPage": perPage}
                  )


def addOffer(response):
    if response.method == "POST":
        form = CreateOffer(response.POST)
        user = response.user
        # if form.is_valid() and (JobOffer.objects.filter(username='myname', status=0).count() <= 3 or user.groups.filter(name="premium").exists()):
        if form.is_valid():
            user = response.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            city = form.cleaned_data['city']
            tel_num = form.cleaned_data['tel_number']
            newOffer = JobOffer(user=user, title=title, text=text, city=city, tel_number=tel_num)
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


def premiumUser(response):
    return render(response, "SZO/premiumUser.html", {})


def logout(response):
    logout(response)
    return render(response, "SZO/home.html", {})


def delete(response, offer_id):
    off = JobOffer.objects.get(pk=offer_id)
    off.delete()
    return redirect('home')
