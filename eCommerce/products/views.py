from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView , DetailView
from .models import Product

# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    context_object_name = 'object_list'

class ProductDetailView(DetailView):
    queryset = Product.objects.filter()
    template_name = 'products/detail.html'
    context_object_name = 'object'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context



