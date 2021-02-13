from django.db import models

# Create your models here.
class Product(models.Model):
    """
    This is the Product model that is used to handle CRUD Operations on products
    """
    name = models.CharField(max_length=50, unique='True')
    price = models.FloatField()
    quantity = models.IntegerField()
