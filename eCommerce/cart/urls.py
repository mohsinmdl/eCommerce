

from django.urls import include, path, re_path
from django.conf import settings
from .views import cart_home, cart_update

app_name = 'cart'
urlpatterns = [

    path('', cart_home , name='home'),
    re_path(r'^predict/$', cart_update, name='update'),

]