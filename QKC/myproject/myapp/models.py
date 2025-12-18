from django.db import models

# Create your models here.
class Index:
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    point = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)