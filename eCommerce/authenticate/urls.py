

from django.urls import include, path, re_path
from django.conf import settings
from .views import login_user, logout_user,register_user,edit_profile,change_password


app_name = 'authenticate'
urlpatterns = [


    path('login/', login_user , name='login'),
    path('logout/', logout_user , name='logout'),
    path('register/', register_user , name='register'),
    path('edit_profile/', edit_profile , name='edit_profile'),
    path('change_password/', change_password , name='change_password'),

]