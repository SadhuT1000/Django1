
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalo/', include('catalog.urls', namespace='catalog')),
    path('contact/', include('catalog.urls', namespace='catalog')),
]
