
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.CharField(max_length=1000)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.item