from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("login/", views.login, name="login"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),

]