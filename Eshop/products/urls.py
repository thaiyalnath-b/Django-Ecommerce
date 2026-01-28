from django.urls import path

from .views import productsView, searchProducts

from .views import CreateProduct, ProductDetail, UpdateProduct, DeleteProduct

from .views import EditProductImage, DeleteProductImage

urlpatterns =[
    path('all/', productsView, name='products'),
    path('search/', searchProducts, name='search_products'),
    
    path('add/', CreateProduct.as_view(), name='add_product'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_details'),
    path('<int:pk>/edit/', UpdateProduct.as_view(), name='edit_product'),
    path('<int:pk>/delete/', DeleteProduct.as_view(), name='delete_product'),

    path('image/edit/<int:pk>', EditProductImage.as_view(), name='edit_product_image'),
    path('image/delete/<int:pk>', DeleteProductImage.as_view(), name='delete_product_image')
]