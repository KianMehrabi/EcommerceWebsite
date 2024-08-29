from django.urls import path

# importing from views
from . import views

urlpatterns = [
    path("view/", views.CartView.as_view(), name="cart_view"),
]
