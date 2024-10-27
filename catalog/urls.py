from django.urls import path

from catalog.apps import CatalogConfig

from .views import ContactView, ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactView.as_view(), name='contact'),]

