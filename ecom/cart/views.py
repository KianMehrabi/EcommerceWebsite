from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.


class CartSummary(TemplateView):
    template_name = "view.html"


class CartAdd(View):
    def post(self, request):
        cart = Cart(request)
        if request.POST.get("action") == "post":
            product_id = int(request.POST.get("product_id"))

            # i want 404 becouse its better than redirect to some page!
            product = get_object_or_404(Product, id=product_id)

            cart.add(product=product)

            response = JsonResponse({"product Name": product.name})
            return response
        else:
            pass


class CartDelete(View):
    pass


class CartUpdate(View):
    pass
