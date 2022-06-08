from django.shortcuts import render
from store.models import Product
from category.models import Category

def home(request):
    products = Product.objects.all().filter(is_available=True)
    category = Category.objects.all().order_by('-created')[0:11]
    featured = Product.objects.all().filter(is_featured=True)
    new = Product.objects.all().filter(is_new=True)
    sale = Product.objects.all().filter(on_sale=True)

    context = {
        'products': products,
        'category': category,
        'featured': featured,
        'new': new,
        'sale': sale,
    }
    return render(request, 'home.html', context)
