

from django.urls import include, path, re_path
from .views import predictView
app_name = 'predictor'
urlpatterns = [

    path('', predictView , name='home'),


]