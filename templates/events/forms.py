from django import forms
from betterforms.multiform import MultiModelForm

from .models import Livraison, Produit, EventImage, EventAgenda


class ProductForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = ['category','name','price', 'stock','image', 'description','volume']
        


class LivraisonForm(forms.ModelForm):
    
    class Meta:
        model = Livraison
        fields = ['produit', 'image', 'price','quantite','ville', 'start_date', 'location','volume']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }  
              
                

        
class ProductImageForm(forms.ModelForm):

    class Meta:
        model = EventImage
        fields = ['image']



class EventAgendaForm(forms.ModelForm):

    class Meta:
        model = EventAgenda
        fields = ['session_name', 'speaker_name', 'start_time', 'end_time', 'venue_name']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class CreateMultiForm(MultiModelForm):
    form_classes = {
        'event': ProductForm,
    }
    
class LivraisonMultiForm(MultiModelForm):
    form_classes = {
        'event': LivraisonForm,
    }
