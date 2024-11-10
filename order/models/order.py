from django.db import models
from django.contrib.auth.models import User

from product.models import Product

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)