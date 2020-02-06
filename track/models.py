from django.db import models
import datetime
# Create your models here.


class Product(models.Model):
    TYPE = (
        ('Tin', 'Tin'),
        ('Glass', 'Glass'),
    )
    PROD_ID = (
        ('SAF_TSD2G-TIN', 'Saffron 2 Gram Tin'),
        ('SAF_TSD1G-GLASS', 'Saffron 1 Gram Glass'),
        ('SAF_TSD2G-GLASS', 'Saffron 2 Gram Glass'),
    )
    product_id = models.CharField(
        max_length=100, choices=PROD_ID, default='TSD2G-TIN')
    size = models.CharField(max_length=20)
    package_type = models.CharField(
        max_length=100, choices=TYPE, default='Tin')
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return (self.product_id + ' PRICE: $'+str(self.price))


class Order(models.Model):
    PACK = (
        ('Zak', 'Zak'),
        ('Adil', 'Adil'),
        ('Yama', 'Yama'),
    )
    name = models.CharField(max_length=15, choices=PACK, default='yama')
    buyer = models.CharField(max_length=20, default='Bob')
    order_id = models.CharField(max_length=100)
    amount_paid = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return (self.name + " SHIPPED: " + str(self.quantity)+", ID: "+self.order_id+", ON: "+str(self.date))


class Expense(models.Model):
    EMP = (
        ('Zak', 'Zak'),
        ('Adil', 'Adil'),
        ('Yama', 'Yama'),
    )
    name = models.CharField(max_length=15, choices=EMP, default='yama')
    reason = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    amount = models.FloatField(default=0.00)

    def __str__(self):
        return (self.name + " SPENT: " + str(self.amount)+", FOR: "+self.reason+", ON: "+str(self.date))


class Invoice(models.Model):
    store = models.CharField(max_length=50)
    invoice_id = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    twoglass = models.IntegerField(default=0)
    oneglass = models.IntegerField(default=0)
    twocan = models.IntegerField(default=0)
    twoglass_p = models.FloatField(default=0.00)
    oneglass_p = models.FloatField(default=0.00)
    twocan_p = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)

    def __str__(self):
        return (self.store + " Total: " + str(self.total))
