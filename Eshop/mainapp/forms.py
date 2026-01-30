from django import forms
from .models import CarouselImage

class CarouselImageForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['img', 'title', 'caption', 'link', 'active']
        widgets = {
            'img': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Carousel title'
            }),
            'caption': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Short description for carousel',
                'rows': 3
            }),
            'link': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Redirect link (optional)'
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
