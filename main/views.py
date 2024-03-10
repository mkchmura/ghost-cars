from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, ProductImage, Category

from django.db.models import Prefetch
from django.conf import settings
from urllib.parse import urljoin

import requests

def index(request):
    response = requests.get('http://wttr.in/Paris?format=%t%w')
    weather_data = response.text

    get_prestige_featured = Product.objects.filter(principal=True, category=1)
    get_sport_featured = Product.objects.filter(principal=True, category=2)

    prestige_products = get_prestige_featured.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )
    sport_products = get_sport_featured.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )

    return render(request, 'test.html', {'prestige_products': prestige_products, 'sport_products': sport_products, 'weather_data': weather_data})

def cars(request, slug):
    product = Product.objects.get(slug=slug)
    images = product.product_image.all()

    base_url = request.build_absolute_uri('/')  # Get the base URL dynamically

    # Generate full URLs for the images
    image_urls = [urljoin(base_url, image.image.url) for image in images]
    return render(request, 'cars.html', {'product': product, 'image_urls': image_urls})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'cars.html', {'product': product})

def list(request):
    get_prestige_featured = Product.objects.filter(category=1)
    get_sport_featured = Product.objects.filter(category=2)

    prestige_products = get_prestige_featured.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )
    sport_products = get_sport_featured.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )
    return render(request, 'all.html', {'prestige_products': prestige_products, 'sport_products': sport_products})

def test(request):
    return render(request, 'test.html')


def about(request):
    return render(request, 'about.html')
    
def all(request):
    cars = Product.objects.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )
    return render(request, 'all.html', {'cars':cars})


def category(request, slug):
    cat = Product.objects.filter(category=slug)
    cars = cat.prefetch_related(
        Prefetch('product_image', queryset=ProductImage.objects.filter(is_feature=True))
    )
    return render(request, 'category.html', {'cars':cars})