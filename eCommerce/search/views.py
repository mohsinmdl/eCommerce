from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q
# Create your views here.

class SearchProductListView(ListView):

    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
        

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request)
        query = request.GET.get('q', None)
        print(query)
        if query is not None:
            lookups = (Q(title__icontains=query)|
                       Q(discription__icontains =query)|
                       Q(tag__title__icontains=query))
            return Product.objects.filter(lookups).distinct()
        return Product.objects.none()




