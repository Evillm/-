from django.urls import path
from .views import payment_view, stripe_webhook

urlpatterns = [
    path('payment/', payment_view, name='payment'),
    path('stripe-webhook/', stripe_webhook, name='stripe-webhook'),
]