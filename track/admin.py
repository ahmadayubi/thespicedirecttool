from django.contrib import admin
from .models import Product, Order, Expense

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Expense)
