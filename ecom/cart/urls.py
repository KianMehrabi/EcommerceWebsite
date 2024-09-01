from django.urls import path

from . import views

urlpatterns = [
    path("", views.CartSummary.as_view(), name="cart_summary"),
    path("add/", views.CartAdd.as_view(), name="cart_add"),
    path("delete/", views.CartDelete.as_view(), name="cart_delete"),
    path("update/", views.CartUpdate.as_view(), name="cart_update"),
]
