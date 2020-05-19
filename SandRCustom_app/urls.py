from django.urls import path
from . import views

urlpatterns = [
    # path('home', views.home),
    path('', views.index),
    path('view_product/<int:id>', views.view_product),
    path('register', views.register),
    path('login', views.login),
    path('rend_index', views.rend_index),
    path('logout', views.logout),
    path('customize/<int:id>', views.customize),
    path('view_cart', views.view_cart),
    # path('add_to_cart/<int:id>', views.add_to_cart),
    path('checkout', views.checkout)
    ]