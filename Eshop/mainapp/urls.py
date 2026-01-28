from django.urls import path

from . import views

from .views import (
    CarouselImageCreateView, CarouselImageListView, CarouselImagesUpdateView, CarouselImageDeleteView
)

urlpatterns = [
    path('', views.homeView, name='home_page'),
    path('about/', views.aboutView, name='about_page'),
    path('contact/', views.contactView, name='contact_page'),

    path('carousels/', CarouselImageListView.as_view(), name='carousel_list'),
    path('carousels/add/', CarouselImageCreateView.as_view(), name='carousel_add'),
    path('carousels/<int:pk>/edit/', CarouselImagesUpdateView.as_view(), name='carousel_edit'),
    path('carousels/<int:pk>/delete/', CarouselImageDeleteView.as_view(), name='carousel_delete')
]

