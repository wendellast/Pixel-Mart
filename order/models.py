from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="c",
        max_length=1,
        # Status
        choices=(
            ("A", "Approved"),
            ("C", "Criated"),
            ("R", "Disapproved"),
            ("P", "Pending"),
            ("S", "Sent"),
            ("F", "finished"),
        ),
    )

    def __str__(self):
        return f"Order Nº {self.pk}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField()
    image = models.URLField(max_length=2000)

    def __str__(self):
        return f"Item: {self.product} - Order: {self.order}"
