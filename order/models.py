from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.models.CharField(
        default="c",
        max_length=1,

        #Status
        choices=(
            ('A', "Approved"),
            ('C', "Criated"),
            ('R', "Disapproved"),
            ('P', "Pending"),
            ('S', "Sent"),
            ('F', "finished")
        )
    )

class OrdenItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    
