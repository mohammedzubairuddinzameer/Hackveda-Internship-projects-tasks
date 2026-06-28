from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from devices import views

urlpatterns = [
path("", views.device_list, name="device_list"),
path("add/", views.device_add, name="device_add"),
path("<int:pk>/", views.device_detail, name="device_detail"),
path("<int:pk>/edit/", views.device_edit, name="device_edit"),
path("<int:pk>/delete/", views.device_delete, name="device_delete"),
path("dashboard/", views.dashboard, name="dashboard"),
path("<int:pk>/buy/", views.buy_device, name="buy_device"),
path("<int:pk>/sell/", views.sell_device, name="sell_device"),
path("<int:pk>/chat/", views.device_chat, name="device_chat"),
]
# Serve media files (images) during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

