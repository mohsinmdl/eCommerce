

from django.urls import include, path, re_path
from django.conf import settings
from .views import cart_home

app_name = 'cart'
urlpatterns = [

    path('', cart_home , name='cart'),

]