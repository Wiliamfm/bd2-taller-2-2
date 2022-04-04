import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import caches

from commerce.models import *

# Create your views here.

#This view is cached, see the urls.py file.
def index(request):
	if request.method == 'GET':
		products= Product.objects.all()
		return render(request, 'commerce/index.html', {
    		'products': products
  		})

def products(request, id):
	if request.method == 'GET':
		product= Product.objects.get(id= id)
		variants= Variant.objects.filter(product= product)
		return render(request, 'commerce/product.html', {
			'product': product,
			'variants': variants
		})

@csrf_exempt
def carts(request):
	if request.method == 'GET':
		cart= 'carts'
		return render(request, 'commerce/cart.html', {
			'cart': cart
		})
	if request.method == 'POST':
		data= json.loads(request.body)
		print(data)
		#Access redis db
		r= caches['default']
		k= f'cart:{data["product_id"]}'
		#Get the variants stored in redis
		variants= r.get(key= k)[0]
		if variants:
			quantity= variants.get(data['variant_id'])
			if quantity:
				#Increment variant quantity
				variants[data['variant_id']]= quantity+1
			else:
				#Save this variant
				variants[data['variant_id']]= 1
			#update value
			r.set(key= k, value= [
				variants
			])
			#Update timeout
			r.touch(key= k, timeout= 60*60)
		else:
			#Save the variant up to 1 hour
			r.set(key= k, value= {data['variant_id']: 1}, timeout= 60*60)
		print(r.get(k))
		return JsonResponse({'message': 'Item added successfully'}, status= 201)