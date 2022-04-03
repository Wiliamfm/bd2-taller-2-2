from itertools import product
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize

from commerce.models import *

# Create your views here.

def index(request):
	if request.method == 'GET':
		products= Product.objects.all()
		return render(request, 'commerce/index.html', {
    		'products': products
  		})

def products(request, id):
	if request.method == 'GET':
		product= Product.objects.get(id= id)
		return render(request, 'commerce/product.html', {
			'product': product
		})

def variants(request, id):
	if request.method == 'GET':
		product= Product.objects.get(id= id)
		variants= Variant.objects.filter(product= product)
		data= serialize('json', variants)
		return JsonResponse(data, safe= False)