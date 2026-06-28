from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def home_redirect(request):
    return redirect('device_list')


urlpatterns = [
    path('', home_redirect),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("devices/", include("devices.urls")),
    path('transactions/', include('transactions.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


