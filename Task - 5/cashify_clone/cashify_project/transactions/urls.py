from django.urls import path
from .views import sell_device

urlpatterns = [
    path('sell/<int:device_id>/', sell_device, name='sell_device'),
]
