

from django.urls import include, path, re_path
from django.conf import settings

from .views import (SearchProductListView,
                            )

app_name = 'search'
urlpatterns = [

    path('', SearchProductListView.as_view(), name='searchProduct'),

]