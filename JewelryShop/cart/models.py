from django.contrib.auth import get_user_model
from django.db import models
from JewelryShop.jewelries.models import Jewelry

# Create your models here.

UserModel = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'jewelry')

    def get_total_price(self):
        return self.quantity * self.jewelry.price