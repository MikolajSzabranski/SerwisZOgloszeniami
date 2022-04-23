from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser, typesUser



class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    typeUser = forms.ChoiceField(choices=typesUser, widget=forms.RadioSelect, initial='Job seeker')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "typeUser"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
