from statistics import mode
from tabnanny import check
from django.shortcuts import render
import stripe
from django.http import JsonResponse
from django.conf import settings
stripe.api_key=settings.STRIPE_SECRET_KEY
# Create your views here.

def product_landing_view(request):
    return render(request, 'landing.html')

def create_checkout_session_view(request):
    YOUR_DOMAIN='http://127.0.0.1:8000'
    checkout_session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'unit_amount':2000,
                    'product_data':{
                        'name': 'Stubborn Attachments',
                        # 'images':['https://i.imgur.com/EHyR2nP.png'],
                    },
                },
                'quantity':1,
            },
        ],
        mode='payments',
        success_url=YOUR_DOMAIN +'/success',
        cancel_url=YOUR_DOMAIN + '/cancel'
    )
    return JsonResponse({
        'id':checkout_session.id
    })