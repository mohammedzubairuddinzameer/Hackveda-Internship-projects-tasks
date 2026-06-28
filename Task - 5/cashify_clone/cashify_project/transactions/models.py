from django.db import models
from django.contrib.auth.models import User
from devices.models import Device

class Transaction(models.Model):
    STATUS_CHOICES = [
        ('initiated', 'Initiated'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    ]

    device = models.OneToOneField(
        Device,
        on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='initiated'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.device}"
