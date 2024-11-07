from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.models import Product, Category
from django.urls import reverse_lazy, reverse
from .froms import ProductsForm

class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductsForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductsForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = 'Это дополнительная информация'
        return context


