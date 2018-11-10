from django.conf.urls import url
from .views import predictView

app_name= 'search'
urlpatterns = [
    url(r'^$', predictView,{}),
]

