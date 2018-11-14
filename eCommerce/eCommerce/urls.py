"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static


from .views import home_page, contact_page, register_page,login_page,register_page
from products.views import (ProductListView,
                            ProductDetailView,
                            ProductFeaturedListView,
                            ProductFeaturedDetailView,
                            ProductSlugDetailView)


app_name = 'products'
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('contact/', contact_page, name='contact'),
    path('products/', include("products.urls")),
    # path('search/', include("search.urls")),
    path('cart/', include("cart.urls")),
    path('auth/', include("authenticate.urls"))


]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)