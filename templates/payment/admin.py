from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'currency', 'status', 'timestamp']
    list_filter = ['status', 'currency']
    search_fields = ['user__username', 'stripe_charge_id']