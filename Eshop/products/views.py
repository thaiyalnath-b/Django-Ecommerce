from django.shortcuts import render

from .models import Product 
# Create your views here.

def productsView(request):
    template = 'products/products.html'
    context = {
        'current_page' : 'products',
        'products' : Product.objects.all()
    }
    
    return render(request, template_name=template, context=context)
