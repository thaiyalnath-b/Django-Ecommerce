from django.shortcuts import render, redirect
from django.urls import reverse

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
    else :
        context ={
            'query' : query,
            'products' : None
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

from django.views.generic.edit import FormMixin
# This mixin provides ability to render forms from the `form_class`
from .forms import ProductImageForm

class ProductDetail(FormMixin, DetailView):
    model = Product
    template_name = 'products/product_details.html'
    # Here we didn't use the success_url, because other 3 are post method there when we do something it goes to another page.
    # Here we using get method. So dont want to use the success_url.
    context_object_name = 'product'
    # providing form class for Product Image
    form_class = ProductImageForm

    def get_success_url(self):
        return reverse("product_details", kwargs={'pk':self.object.pk})

    # Overriding the queryset to pre-fetch and add the product images alongside products
    def get_queryset(self):
        return Product.objects.prefetch_related('images')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            image = form.save(commit = False)
            image.product = self.object
            image.save()
            return redirect(self.get_success_url())


    # If we want to add extra data then we can use this method.
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['ExtraDetail'] = 'This is Extra Added Detail'
    #     return context

class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    fields = '__all__'
    success_url = '/'

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = '/'


# Edit Product Image
from .models import ProductImage

class EditProductImage(UpdateView):
    model = ProductImage
    template_name = 'products/image_edit.html'
    fields = '__all__'
    context_object_name = 'image'

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk':self.object.product.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object.product
        return context
    

class DeleteProductImage(DeleteView):
    model = ProductImage
    template_name = 'products/image_delete.html'
    context_object_name = 'image'

    def get_success_url(self):
        return reverse('product_details', kwargs={'pk':self.object.product.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object.product
        return context
    