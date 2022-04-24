from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser, typesUser, JobOffer


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

class CreateOffer(forms.Form):
    text = forms.CharField(max_length=1000)
    title = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    tel_number = forms.IntegerField(help_text='Enter telephone number:')

    class Meta:
        model = JobOffer
        fields = ('title', 'text', 'city', 'tel_number')
