from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from paywix.payu import Payu
from django.contrib.auth.models import Group

from SerwisZOgloszeniami.settings import PAYU_CONFIG

payu_config = PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

# Create payu instance
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)
data = {
    'amount': '10', 'firstname': 'renjith',
    'email': 'renjithsraj@gmail.com',
    'phone': '9746272610',
    'productinfo': 'test',
    'lastname': 'test',
    'address1': 'test',
    'address2': 'test',
    'city': 'test',
    'state': 'test',
    'country': 'test',
    'zipcode': 'test',
    'udf1': '',
    'udf2': '',
    'udf3': '',
    'udf4': '',
    'udf5': ''
}
# Make sure the transaction ID is unique
txnid = "Create your transaction id"
data.update({"txnid": txnid})
payu_data = payu.transaction(**data)


class PayuView(View):
    template_name = 'SZO/payu.html'

    def get(self, request, *args, **kwargs):
        import uuid
        payload = {
            "amount": 30,
            "firstname": "John",
            "lastname": "Wick",
            "email": "example@live.com",
            "phone": 9746272610,
            "productinfo": "Premium Account",
            "address1": "Test address 1",
            "address2": "Test Address 2",
            "city": "Test city",
            "state": "Test state",
            "country": "Test country",
            "zipcode": 673576,
            "txnid": uuid.uuid1()
        }
        return render(request, self.template_name, {'posted': payload})

    def post(self, request, *args, **kwargs):
        print("Inside Class Based View")
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        payu_data = payu.transaction(**data)
        return render(request, 'SZO/checkout.html', {"posted": payu_data})


# Payu Checkout
@csrf_exempt
def payu_checkout(request):
    if request.method == 'POST':
        data = {k: v[0] for k, v in dict(request.POST).items()}
        data.pop('csrfmiddlewaretoken')
        payu_data = payu.transaction(**data)
        return render(request, 'SZO/checkout.html', {"posted": payu_data})
    return render(request, 'SZO/payu.html', {'posted': ""})


# Payu failure page
@csrf_exempt
def payu_failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)


# Payu success return page
@csrf_exempt
def payu_success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)
