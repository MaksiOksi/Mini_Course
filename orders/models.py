from django.contrib.auth.models import User
from django.db import models

from products.models import Product


# Menu
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
