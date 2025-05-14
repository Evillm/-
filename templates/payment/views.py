import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def payment_view(request):
    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
                amount=10000,  # المبلغ بالقرش عن الطلب
                currency='egp',
                description='طلب من المتجر العضوي',
                source=request.POST['stripeToken']
            )
            return render(request, 'payment/success.html')
        except stripe.error.CardError:
            return render(request, 'payment/fail.html')

    return render(request, 'payment/payment.html', {
        'stripe_pub_key': settings.STRIPE_PUBLIC_KEY
    })