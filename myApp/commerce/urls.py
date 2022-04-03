from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    #Cache the result of the index function fo the views module for 10 min.
    path('', cache_page(60*10)(views.index), name='index'),
    path('products/<int:id>/', views.products, name='products'),
    path('products/<int:id>/variants', views.variants, name='variants')
]