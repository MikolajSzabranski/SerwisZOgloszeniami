from django.urls import path

from PayU.views import *

urlpatterns = [
    path('premiumUser/payu/', PayuView.as_view(), name='payu'),
    path('premiumUser/payu_checkout/', payu_checkout, name="checkout"),
    path('payu/failure/', payu_failure, name="payufailure"),
    path('payu/success/', payu_success, name="payusuccess"),
]