from django.contrib.auth import get_user_model
from django.db import models

from JewelryShop.common.choices import RatingChoices
from JewelryShop.jewelries.models import Jewelry


UserModel = get_user_model()

class Reviews(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=300)
    rating = models.IntegerField(choices=RatingChoices.choices)
    date_of_publication = models.DateField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    shipping_address = models.TextField(max_length=100)
    phone = models.CharField(max_length=11)
    date = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    