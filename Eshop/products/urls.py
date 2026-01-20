from django.urls import path

from . import views

urlpatterns =[
    path('all/', views.productsView, name='products'),
    path('search/',views.searchProducts, name='search_products')
]