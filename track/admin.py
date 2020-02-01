from django.contrib import admin
from .models import Product, Order, Expense, Invoice

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Expense)
admin.site.register(Invoice)
