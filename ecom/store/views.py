from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View

# you need this for the CBVs succes url to redirect to a url_name!
from django.urls import reverse_lazy

from .forms import CreatingUserForm
from .models import Product


def home_page(request):
    products = Product.objects.all()
    return render(request, "pages/home.html", {"products": products})


def about_page(request):
    return render(request, "pages/about.html", {})


def login_user(request):
    if request.user.is_authenticated:
        messages.error(request, ("you are already Registered and Loged in"))
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Loged In"))
            return redirect("home")
        else:
            messages.error(request, ("There was a Error"))
            return redirect("login")
    else:
        return render(request, "pages/login.html", {})


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Loged out"))
    return redirect("home")


class RegisterUser(View):
    template_name = "pages/register.html"
    form_class = CreatingUserForm

    def get(self, request):
        if request.user.is_authenticated:
            messages.error(request, ("you are already Registered and Loged in"))
            return redirect("home")
        form = self.form_class
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            messages.error(request, ("you are already Registered and Loged in"))
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, ("you are Registered and Loged in"))
                return redirect("home")
        messages.error(request, ("there was an Error"))
        return render(request, self.template_name, context={"form": form})


class ProductPage(View):
    template_name = "pages/product.html"

    def get(self, requeset, id, *args, **kwargs):
        model = Product.objects.get(id=id)
        return render(
            requeset,
            self.template_name,
            context={"product": model},
        )
