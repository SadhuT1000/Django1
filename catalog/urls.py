from django.urls import path, include
from . import views
from catalog.apps import CatalogConfig
from django.contrib import admin

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('info/<int:product_id>/', views.info, name='info'),
    path('all_products/', views.all_products, name='all_products'),
]
