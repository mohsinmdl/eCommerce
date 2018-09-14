

from django.urls import include, path, re_path
from django.conf import settings

from .views import (ProductListView,
                            ProductDetailView,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView,
                            ProductSlugDetailView)

urlpatterns = [

    path('', ProductListView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductSlugDetailView.as_view()),

]