from django.urls import path, include
from . import views
from catalog.apps import CatalogConfig
from django.contrib import admin
from .views import ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int>:product_id/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),]

    # path('home/', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('info/<int:product_id>/', views.info, name='info'),
    # path('all_products/', views.all_products, name='all_products'),

