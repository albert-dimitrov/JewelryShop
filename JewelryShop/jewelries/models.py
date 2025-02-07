from django.db import models

from JewelryShop.jewelries.choices import CategoryChoices


class Jewelry(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(null=True, blank=True) #For a production it is good to be images uploaded to cloud
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} --> {self.stock} in stock'
