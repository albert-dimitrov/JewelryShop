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
    product = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=11)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)