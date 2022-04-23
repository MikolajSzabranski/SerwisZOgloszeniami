from django.db import models
from django import forms

# Create your models here.

typesUser = (('Job seeker', 'Job seeker'), ('Host', 'Host'))


class CustomUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    typeUser = models.CharField(max_length=100, choices=typesUser, null=True)
