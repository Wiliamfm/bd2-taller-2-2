from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    #Cache the result of the index function fo the views module for 10 min.
    path('', cache_page(60*10)(views.index), name='index'),
    path('products/<int:id>/', views.products, name='products'),
    path('cart/', views.carts, name='cart'),
    path('buy/', views.bills, name='bills'),
    path('pay_methods/', views.pay_methods, name= 'pay_methods')
]