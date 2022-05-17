from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/google/login/', auth_views.LoginView.as_view(template_name="registration/login.html"),
    #      name="loginGoogle"),

    path("", views.home, name="home"),
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("offer/", views.offer, name="offer"),
    path("logout/", views.logout, name="logout"),
    path("addOffer/", views.addOffer, name="addOffer"),
    path("premiumUser/", views.premiumUser, name="premiumUser"),
    path("delete/<offer_id>", views.delete, name="delete"),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="passwordReset/password_reset_form.html"),
         name='password_reset'),
    path('password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(template_name="passwordReset/password_reset_done.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="passwordReset/password_reset.html"),
         name='password_reset_confirm'),
    path('reset_done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="passwordReset/password_reset_complete.html"),
         name='password_reset_complete'),

]
