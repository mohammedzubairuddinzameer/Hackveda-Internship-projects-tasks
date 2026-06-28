from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        exclude = ["user"]  # 🔥 VERY IMPORTANT

