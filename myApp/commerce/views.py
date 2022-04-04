import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import caches

from commerce.models import *

import pymongo

client= pymongo.MongoClient()
db= client['commerce']
col= db['bill']

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
	r= caches['default']
	key_products= 'cart:products'
	if request.method == 'GET':
		products_id= r.get(key_products)
		if products_id:
			products= []
			for product in Product.objects.filter(id__in=products_id):
				vs= r.get(f'cart:{product.id}')[0]
				variants= []
				for v in vs:
					variant= Variant.objects.get(product= product, id= v)
					variants.append({'variant': variant, 'qty': vs[v]})
				products.append({'product': product, 'variants': variants})
			#Save cart in cache memory
			r.set(key= 'cart', value= products, timeout= 60*60*2)
			return render(request, 'commerce/cart.html', {
				'has_items': True,
				'products': products,
			})
		else:
			return render(request, 'commerce/cart.html', {
				'has_items': False
			})
	if request.method == 'POST':
		data= json.loads(request.body)
		print(data)
		#Access redis db
		#Get the variants stored in redis
		products= r.get(key= key_products)
		#Save the product
		if products:
			products.add(data['product_id'])
			r.set(key= key_products, value=products)
			r.touch(key= key_products, timeout= 60*60)
		else:
			r.set(key= key_products, value= {data['product_id']}, timeout= 60*60)
		key_variants= f'cart:{data["product_id"]}'
		variants= r.get(key= key_variants)
		if variants:
			quantity= variants[0].get(data['variant_id'])
			if quantity:
				#Increment variant quantity
				variants[0][data['variant_id']]= quantity+1
			else:
				#Save this variant
				variants[0][data['variant_id']]= 1
			#update value
			r.set(key= key_variants, value= [
				variants[0]
			])
			#Update timeout
			r.touch(key= key_variants, timeout= 60*60)
		else:
			#Save the variant up to 1 hour
			r.set(key= key_variants, value= [{data['variant_id']: 1}], timeout= 60*60)
		print(r.get(key_variants))
		return JsonResponse({'message': 'Item added successfully'}, status= 201)

@csrf_exempt
def bills(request):
	if request.method == 'POST':
		r= caches['default']
		products= r.get('cart')
		data= json.loads(request.body)
		for product in products:
			p= {'product': product['product'].as_dict()}
			vs= []
			for variant in product['variants']:
				v= variant['variant'].as_dict()
				v.update({'quantity': variant['qty']})
				vs.append(v)
			p['variants']= vs
			p['pay_method']= data['pay_method']
			p['address']= data['address']
			col.insert_one(p)
	return render(request, 'commerce/buy.html')

def pay_methods(request):

	def as_dict(pay_methods):
		d= []
		for pm in pay_methods:
			d.append({'pay_method': pm.pay_method})
		return d

	if request.method == 'GET':
		pms= PayMethod.objects.all()
		pay_methods= as_dict(pms)
		return JsonResponse(pay_methods, status= 200, safe= False)
