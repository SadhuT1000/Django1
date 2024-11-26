from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .froms import ProductsForm, ProductsModeratorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.views import View

from catalog.services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductsForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductsForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductsForm
        if user.has_perm('product.can_unpublish_product'):
            return ProductsModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):

        product = super().get_object(queryset)
        user = self.request.user

        if product.owner != user and not user.has_perm('catalog.can_delete_product'):
            raise PermissionDenied("Вы не можете удалять этот продукт.")

        return product

class ProductsByCategoryView(ListView):
    model = Category
    def get_queryset(self):
        category_id = self.kwargs.get('pk')
        return get_products_by_category(category_id=category_id)





class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = 'Это дополнительная информация'
        return context
