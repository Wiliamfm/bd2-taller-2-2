from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:id>/', views.products, name='products'),
    path('products/<int:id>/variants', views.variants, name='variants')
]