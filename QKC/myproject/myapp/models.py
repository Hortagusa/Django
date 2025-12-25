
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
        STATUS_CHOICES = [
            ('pending', 'Chờ xử lý'),
            ('confirmed', 'Đã xác nhận'),
            ('shipping', 'Đang giao'),
            ('done', 'Hoàn thành'),
            ('cancel', 'Đã hủy'),
        ]

        firstName = models.CharField(max_length=200)
        lastName = models.CharField(max_length=200)
        address = models.TextField()
        phone = models.CharField(max_length=100)
        email = models.EmailField()

        items = models.TextField()  # lưu JSON giỏ hàng
        total = models.FloatField(default=0)

        status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default='pending'
        )

        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Order #{self.id} - {self.firstName}"

