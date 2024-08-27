from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import FormView

# you need this for the CBVs succes url to redirect to a url name!
from django.urls import reverse_lazy

from .forms import CreatingUserForm
from .models import Product


def home_page(request):
    products = Product.objects.all()
    return render(request, "pages/home.html", {"products": products})


def about_page(request):
    return render(request, "pages/about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Loged In"))
            return redirect("home")
        else:
            messages.success(request, ("There was a Error"))
            return redirect("login")
    else:
        return render(request, "pages/login.html", {})


@login_required(login_url="login")
def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Loged out"))
    return redirect("home")


class RegisterUser(FormView):
    template_name = "pages/register.html"
    form_class = CreatingUserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
