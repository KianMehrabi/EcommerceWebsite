from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from .models import Product

def home_page(request):
    products = Product.objects.all()
    return render(request , "pages/home.html" , {"products":products})

def about_page(request):
    return render(request ,"pages/about.html" , {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request , ("You Have Been Loged In"))
            return redirect('home')
        else:
            messages.success(request , ("There was a Error"))
            return redirect('login')
    else:
        return render(request , "pages/login.html" , {})