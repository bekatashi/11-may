from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
