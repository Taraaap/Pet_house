from django.contrib import admin
from .models import Product, Contact,Order
# Register your models here.

admin.site.register(Contact)
admin.site.register(Product)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'product', 'status', 'payment_method', 'created_at')
    list_filter = ('status', 'payment_method')
    ordering = ('-created_at',)