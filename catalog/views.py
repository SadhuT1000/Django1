from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.models import Product, Category
from django.urls import reverse_lazy, reverse

class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ('names', 'description', 'price', 'group')
    success_url = reverse_lazy('catalog:products_list')

class ProductDetailView(DetailView):
    model = Product

    def get_odject(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('names', 'description', 'price', 'group')
    success_url = reverse_lazy('catalog:products_list')

    def get_success_url(self):
        return reverse('catalog:products_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')



#
# from catalog.models import Product, Category
# # Create your views here.
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
#
#
# def home(request):
#     return render(request, 'catalog/home.html')
#
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')
#
#
# def info(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#
#     context = {
#        'product': product
#     }
#     return render(request, template_name='catalog/info.html', context=context)
#
#
# def all_products(request):
#
#     products = Product.objects.all()
#
#     context = {
#         'products': products,
#     }
#
#     return render(request, template_name='catalog/all_products.html', context=context)