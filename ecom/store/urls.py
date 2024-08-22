from django.urls import path

# importing from views
from .views import *

from . import views
urlpatterns = [
    path('' , home_page , name="home"),
    path('About/' , about_page , name="about"),
    path('LogIn/' , login_user , name="login"),
]
