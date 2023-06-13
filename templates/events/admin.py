from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import (
    Categorie,
    Fournisseur,
    Livraison,
    Produit,
    Client,
    Livreur,
    EventJobCategoryLinking,
    EventMember,
    UserCoin,
)

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Livreur)
admin.site.register(Livraison, MapAdmin)
admin.site.register(EventJobCategoryLinking)
admin.site.register(EventMember)
admin.site.register(Fournisseur)
admin.site.register(UserCoin)
