from django.shortcuts import render
from .cart import Cart
from shop.models import Product
from django.shortcuts import redirect

# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)

    return redirect("Shop")

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)

    return redirect("Shop")

def substract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product=product)

    return redirect("Shop")

def empty_cart(request, product_id):
    cart = Cart(request)
    cart.emtpy_cart()

    return redirect("Shop")