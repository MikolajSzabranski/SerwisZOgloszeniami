from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("offer/", views.offer, name="offer"),
    path("logout/", views.logout, name="logout"),

]