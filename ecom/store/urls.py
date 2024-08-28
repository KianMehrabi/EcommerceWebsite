from django.urls import path

# importing from views
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("product/<int:id>/", views.ProductPage.as_view(), name="product"),
    path(
        "category/<int:category_name>/", views.CatagoryPage.as_view(), name="category"
    ),
]
