
from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ShopListView(ListView):
    model = Product
    template_name = 'shop/Green_corner.html'
    context_object_name = 'products'
