from django.db import models

# Create your models here.
class Product:
    name = models.CharField(max_length=50)

class Index:
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    point = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)

class About:
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    point = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)