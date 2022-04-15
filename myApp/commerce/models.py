# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import N
from turtle import ondrag
from django.db import models


class AppUser(models.Model):
    document = models.CharField(primary_key=True, max_length=20)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=100, null= False)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.ForeignKey('UserType', on_delete= models.CASCADE, db_column='user_type')
    document_type = models.ForeignKey('DocumentType', on_delete= models.SET_NULL, db_column='document_type', null= True)
    city = models.ForeignKey('City', on_delete= models.SET_NULL, db_column='city', null= True)

    class Meta:
        managed = False
        db_table = 'app_user'


class Bill(models.Model):
    total = models.DecimalField(max_digits=20, decimal_places=4)
    bill_date = models.DateTimeField(auto_now_add= True, null= False)
    shopping_cart = models.OneToOneField('ShoppingCart', on_delete= models.SET_NULL, db_column='shopping_cart', blank=True, null= True, unique= True)
    shipping_type = models.ForeignKey('ShippingType', on_delete= models.SET_NULL, db_column='shipping_type', null= True)
    pay_method = models.ForeignKey('PayMethod', on_delete= models.SET_NULL, db_column='pay_method', null= True)
    bill_state = models.ForeignKey('BillState', on_delete= models.SET_NULL, db_column='bill_state', null= True)

    class Meta:
        managed = False
        db_table = 'bill'


class BillState(models.Model):
    bill_condition = models.CharField(unique=True, max_length=40, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'bill_state'


class Brand(models.Model):
    name = models.CharField(unique=True, max_length=100, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'brand'


class CartCondition(models.Model):
    condition = models.CharField(max_length=10, unique= True, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'cart_condition'


class Category(models.Model):
    category = models.CharField(unique=True, max_length=20, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    city = models.CharField(unique=True, max_length=100, null= False)

    class Meta:
        managed = False
        db_table = 'city'


class DocumentType(models.Model):
    type = models.CharField(unique=True, max_length=3, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'document_type'


class PayMethod(models.Model):
    pay_method = models.CharField(unique=True, max_length=20, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'pay_method'


class Phone(models.Model):
    phone = models.CharField(unique=True, max_length=10, null= False, blank= False)
    owner = models.ForeignKey(AppUser, on_delete= models.CASCADE, db_column='owner', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'phone'


class Product(models.Model):
    title = models.CharField(max_length=100, null= False)
    photos = models.BinaryField(blank=True, null=True)  # This field type is a guess.
    price = models.DecimalField(max_digits=13, decimal_places=2, null= False)
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, db_column='brand')
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, db_column='category', blank=True, null=True)
    supplier = models.ForeignKey(AppUser, on_delete= models.CASCADE, db_column='supplier', blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'product'
    
    '''
    def __str__(self) -> str:
        return f"{self.id}"
    '''

    def as_dict(self):
        return {'id': self.id, 'title': self.title, 'brand': self.brand.name, 'category': self.category.category, 'supplier': self.supplier.document}

class ProductCalification(models.Model):
    calification = models.IntegerField(null= False)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, db_column='product', blank=True, null=True)
    bill = models.ForeignKey(Bill, on_delete= models.CASCADE, db_column='bill', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_calification'


class ShippingType(models.Model):
    type = models.CharField(unique=True, max_length=20, null= False, blank= False)

    class Meta:
        managed = False
        db_table = 'shipping_type'


class ShoppingCart(models.Model):
    amount = models.IntegerField(null= False)
    cart_condition = models.ForeignKey(CartCondition, on_delete= models.SET_NULL, db_column='cart_condition', null= True)
    app_user = models.ForeignKey(AppUser, on_delete= models.SET_NULL, db_column='app_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'


class ShoppingProduct(models.Model):
    variant = models.ForeignKey('Variant', on_delete= models.SET_NULL, db_column='variant', blank=True, null=True)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete= models.SET_NULL, db_column='shopping_cart', null= True)

    class Meta:
        managed = False
        db_table = 'shopping_product'


class UserType(models.Model):
    type = models.CharField(max_length=20, blank=False, null=False, unique= True)

    class Meta:
        managed = False
        db_table = 'user_type'


class Variant(models.Model):
    stock = models.IntegerField(null= False)
    description = models.TextField(null= False)
    product = models.ForeignKey(Product, on_delete= models.CASCADE, db_column='product')

    class Meta:
        managed = False
        db_table = 'variant'
    
    '''
    def __str__(self) -> str:
        return f"{self.id}"
    '''
    def as_dict(self):
        return {'id': self.id, 'stock': self.stock, 'description': self.description}