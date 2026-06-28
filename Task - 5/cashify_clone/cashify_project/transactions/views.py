from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from devices.models import Device
from .models import Transaction

@login_required
def sell_device(request, device_id):
    device = get_object_or_404(Device, id=device_id, is_sold=False)

    # Only owner can sell
    if device.owner != request.user:
        return redirect('device_detail', pk=device.id)

    Transaction.objects.create(
        device=device,
        seller=request.user,
        final_price=device.price,
        status='completed'
    )

    device.is_sold = True
    device.save()

    return redirect('device_list')

