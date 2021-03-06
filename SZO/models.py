from django.contrib.auth.models import User
from django.db import models

# Create your models here.

typesUser = (('seeker', 'Seeker'), ('host', 'Host'))


# class CustomUser(models.Model):
#     username = models.CharField(max_length=20)
#     email = models.EmailField(blank=True)
#     password1 = models.CharField(max_length=30)
#     password2 = models.CharField(max_length=30)
#     typeUser = models.CharField(max_length=100, choices=typesUser, null=True)


class JobOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=1000)
    city = models.CharField(max_length=100, default='Warszawa')
    tel_number = models.CharField(max_length=9)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    latitude = models.CharField(max_length=200,default=0)
    longitude = models.CharField(max_length=200, default=0)

    def __str__(self):
        return self.text

    def getText(self):
        return self.text

    def getTitle(self):
        return self.title

    def getCity(self):
        return self.city

    def getTel(self):
        return self.tel_number

    def getUser(self):
        return self.user

    def getUsername(self):
        return str(self.user)

    def getLatitude(self):
        return str(self.latitude)

    def getLongitude(self):
        return str(self.longitude)
