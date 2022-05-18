from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
# from matplotlib import widgets
from .models import typesUser, JobOffer
from django.forms import HiddenInput, ModelForm, TextInput, EmailInput, PasswordInput, ChoiceField, RadioSelect, \
    CharField
from django.core.validators import RegexValidator


class RegisterForm(UserCreationForm):
    email = EmailInput()
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'pass', 'style': 'max-width: 25vw', 'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class': 'pass', 'style': 'max-width: 25vw', 'placeholder': 'password'}),
    )
    typeUser = ChoiceField(
        choices=typesUser, widget=RadioSelect, initial='Job seeker')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "typeUser"]
        widgets = {
            'username': TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 25vw;', 'placeholder': 'Username'}),
            'email': TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 25vw;', 'placeholder': 'example@gmail.com'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 25vw;', 'placeholder': 'Username'}),
            'email': TextInput(
                attrs={'class': "form-control", 'style': 'max-width: 25vw;', 'placeholder': 'example@gmail.com'})
        }


class CreateOffer(ModelForm):
    title = TextInput()
    text = TextInput()
    city = TextInput()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    tel_number = models.CharField(validators=[phoneNumberRegex], max_length=9, unique=True)
    image = models.ImageField(upload_to='images/')
    latitude = TextInput()
    longitude = TextInput()

    class Meta:
        model = JobOffer
        fields = ('title', 'text', 'city', 'tel_number', 'image', 'latitude', 'longitude')
        widgets = {
            'title': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'text': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'city': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'tel_number': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'latitude': HiddenInput(attrs={'id': 'latitude'}),
            'longitude': HiddenInput(attrs={'id': 'longitude'}),
        }
