from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .models import Device

# --------------------
# HOME (ROOT HANDLER)
# --------------------
@login_required(login_url='/accounts/login/')
def home(request):
    return redirect('device_list')


# --------------------
# DEVICE FORM
# --------------------
class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = [
        "name",
        "brand",
        "condition",
        "price",
        "description",
        "image",
        ]


# --------------------
# DEVICE LIST
# --------------------
@login_required
def device_list(request):
    query = request.GET.get('q')

    devices = Device.objects.filter(is_sold=False).order_by("-id")

    if query:
        devices = devices.filter(name__icontains=query)

    return render(request, 'devices/device_list.html', {
        'devices': devices
    })



# --------------------
# DEVICE CREATE
# --------------------
@login_required
def device_create(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            device = form.save(commit=False)
            device.owner = request.user
            device.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'devices/device_form.html', {'form': form})


# --------------------
# DEVICE UPDATE
# --------------------
@login_required
def device_update(request, pk):
    device = get_object_or_404(Device, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'devices/device_form.html', {'form': form})


# --------------------
# DEVICE DETAIL
# --------------------
@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'devices/device_detail.html', {'device': device})

# --------------------
# DASHBOARD
# --------------------
@login_required
def dashboard(request):
    my_devices = Device.objects.filter(user=request.user)
    sold = my_devices.filter(is_sold=True)
    active = my_devices.filter(is_sold=False)

    return render(request, 'devices/dashboard.html', {
        'my_devices': my_devices,
        'sold': sold,
        'active': active,
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Device
from .forms import DeviceForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Device
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Device, ChatMessage


@login_required
def device_list(request):

    devices = Device.objects.all().order_by("-id")

    # Search
    query = request.GET.get("q")
    brand = request.GET.get("brand")

    if query:
        devices = devices.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if brand:
        devices = devices.filter(brand__icontains=brand)

    # Pagination
    paginator = Paginator(devices, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "devices/device_list.html", {
        "page_obj": page_obj
    })



@login_required
def device_add(request):

    if request.method == "POST":
        form = DeviceForm(request.POST, request.FILES)

        if form.is_valid():
            device = form.save(commit=False)
            device.user = request.user
            device.save()

            return redirect("device_list")

        else:
            print(form.errors)  # debug

    else:
        form = DeviceForm()

    return render(request, "devices/device_form.html", {"form": form})


@login_required
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, "devices/device_detail.html", {
    "device": device
    })


@login_required
def dashboard(request):

    my_devices = Device.objects.filter(user=request.user)

    return render(request, "devices/dashboard.html", {
        "devices": my_devices
    })

@login_required
def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)

    # Optional safety: only owner can edit
    if device.user != request.user:
        return redirect("dashboard")

    if request.method == "POST":
        form = DeviceForm(request.POST, request.FILES, instance=device)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = DeviceForm(instance=device)

    return render(request, "devices/device_form.html", {"form": form})


@login_required
def device_delete(request, pk):
    my_devices = Device.objects.filter(user=request.user)

    if request.method == "POST":
        device.delete()
        return redirect("dashboard")

    return render(request, "devices/device_confirm_delete.html", {"device": device})

@login_required
def sell_device(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if device.user != request.user:
        return redirect("device_list")

    device.is_sold = True
    device.save()

    messages.success(request, "Device marked as sold.")
    return redirect("dashboard")

@login_required
def buy_device(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if not device.is_sold and device.user != request.user:
        device.is_sold = True
        device.buyer = request.user
        device.save()

    return redirect("dashboard")

@login_required
def device_chat(request, pk):

    device = get_object_or_404(Device, pk=pk)

    if request.method == "POST":
        text = request.POST.get("message")

        if text:
            ChatMessage.objects.create(
                device=device,
                user=request.user,
                message=text
            )

        return redirect("device_chat", pk=pk)

    messages = ChatMessage.objects.filter(
        device=device
    ).order_by("timestamp")

    return render(request, "devices/device_chat.html", {
        "device": device,
        "messages": messages
    })
