from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    TYPES = (
        ('In Door', 'In Door'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=200, choices=TYPES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
