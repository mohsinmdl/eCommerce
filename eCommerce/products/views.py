from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404


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


class ProductFeaturedListView(ListView):
    queryset = Product.objects.filter(feature=True)
    template_name = 'feature/list.html'
    context_object_name = 'object_list'


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.filter()
    template_name = 'feature/detail.html'
    context_object_name = 'object'


class ProductSlugDetailView(DetailView):
    queryset = Product.objects.filter()
    template_name = 'feature/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Product Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance
