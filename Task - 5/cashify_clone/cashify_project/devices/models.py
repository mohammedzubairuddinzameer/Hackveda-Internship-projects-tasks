from django.db import models
from django.contrib.auth.models import User


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="purchased_devices"
    )

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField()
    condition = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="devices/", null=True, blank=True)

    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ChatMessage(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}"
