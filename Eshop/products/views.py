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


# CRUD Operations using Generic Class Based Views of Django

from django.views.generic import (CreateView, DetailView,
                                        UpdateView, DeleteView) # In python imports are from only one line but sometimes we need to 
                                                                # to import more so that we can use () to cut it to two lines or
                                                                # more based on how many data we import.
                                                                

# ListView has already been implemented using a function above: productsView(). List view is used for Listing the prouducts.

class CreateProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    fields = '__all__'
    success_url = '/'   # redirection url for successful creation of resource

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    # Here we didn't use the success_url, because other 3 are post method there when we do something it goes to another page.
    # Here we using get method. So dont want to use the success_url.
    context_object_name = 'product'

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    fields = '__all__'
    success_url = '/'