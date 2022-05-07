from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from matplotlib import widgets
from .models import typesUser, JobOffer
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, ChoiceField, RadioSelect


class RegisterForm(UserCreationForm):
    email = EmailInput()

    typeUser = ChoiceField(
        choices=typesUser, widget=RadioSelect, initial='Job seeker')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "typeUser"]
        widgets = {
            'username': TextInput(attrs={'class': "form-control", 'style': 'max-width: 400px;', 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': "form-control", 'style': 'max-width: 400px;', 'placeholder': 'Email'}),
            #Nie działa
            'password1': PasswordInput(attrs={'class': "form-control", 'style': 'max-width: 400px;', 'placeholder': 'Password'}),
            'password2': PasswordInput(attrs={'class': "form-control", 'style': 'max-width: 400px;', 'placeholder': 'Repeat your password'})
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CreateOffer(ModelForm):
    title = TextInput()
    text = TextInput()
    city = TextInput()
    tel_number = forms.IntegerField(
        max_value=999999999, min_value=100000000, help_text='Enter telephone number:')

    class Meta:
        model = JobOffer
        fields = ('title', 'text', 'city', 'tel_number')
        widgets = {
            'title': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'text': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'city': TextInput(attrs={'class': 'offer-form-control', 'style': 'max-width: 25vw'}),
            'tel_number': forms.IntegerField(),
        }
