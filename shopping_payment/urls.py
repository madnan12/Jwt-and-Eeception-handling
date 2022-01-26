from django.urls import path
from shopping_payment import views

urlpatterns = [
    path('', views.product_landing_view),
]
