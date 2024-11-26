from django.urls import path

from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

from .views import (ContactView, ProductListView, ProductCreateView, ProductDeleteView,
                    ProductDetailView, ProductUpdateView, ProductsByCategoryView)

app_name = CatalogConfig.name

urlpatterns = [
    path('products/', cache_page(60)(ProductListView.as_view()), name='products_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('category/<int:pk>/', ProductsByCategoryView.as_view(), name='products_by_category')
]

