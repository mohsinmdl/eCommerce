

from django.urls import include, path, re_path
from django.conf import settings

from .views import (ProductListView,
                            ProductDetailView,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView,
                            ProductSlugDetailView)

app_name = 'products'
urlpatterns = [

    path('', ProductListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail'),

]