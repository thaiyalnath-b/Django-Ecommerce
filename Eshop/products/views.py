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

# search Products
from django.db.models import Q  
def searchProducts(request):
    template = 'products/search_results.html'
    query = request.GET.get('query_text')
    if query:
        search_results = Product.objects.filter(
            Q(title__icontains = query) |
            Q(desc__icontains = query)      # Here the Q is query set above we import the model for this queryset. we use Q for OR operations in filter.
        )

        context = {
            'query' : query,
            'products' : search_results
        }
    return render(request, template_name=template, context=context)