from django.db import models

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


class Packager(models.Model):
    PACK = (
        ('Zak', 'Zak'),
        ('Adil', 'Adil'),
        ('Yama', 'Yama'),
    )
    name = models.CharField(max_length=15, choices=PACK, default='yama')
    packaged_can = models.IntegerField(default=0)
    packaged_usa = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return (self.name + " HAS: " + str(self.quantity)+", SHIPPED TO CAD: "+str(self.packaged_can)+", SHIPPED TO USA: "+str(self.packaged_usa))
