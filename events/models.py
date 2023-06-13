from django.conf import settings
from django.db import models
from django.urls import reverse
from mapbox_location_field.models import LocationField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _



 # Création Model Categorie



class Categorie(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=6, unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disponible', 'Disponible'),
        ('rupture de stock', 'Rupture de stock'),
        ('emdommagé', 'Endommagé'),
        
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-category-list')
    
    
 # Création Model CLient



class Client(models.Model):
    SEX_TYPES = (
        ('M', _('Male')),
        ('F', _('Feminin')),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    address = models.CharField(max_length=64)
    sexe = models.CharField(max_length=1, choices=SEX_TYPES)
    city = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by_%(class)s_related', on_delete=models.CASCADE)
    updated_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_by_%(class)s_related', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('actif', 'actif'),
        ('inactif', 'Inactif'),
        ('bloqué', 'bloqué'),
        
    )
    status = models.CharField(choices=status_choice, max_length=10)
    
    def get_absolute_url(self):
        return reverse('event-wish-list')
   
    
class Livreur(models.Model):
    SEX_TYPES = (
        ('M', _('Male')),
        ('F', _('Feminin')),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    addresse = models.CharField(max_length=64)
    sexe = models.CharField(max_length=1, choices=SEX_TYPES)
    created_date = models.DateTimeField(auto_now_add=True)
    status_choice = (
        ('actif', 'Actif'),
        ('inactif', 'Inactif'),
        ('bloqué', 'Bloqué'),
    )
    status = models.CharField(choices=status_choice, max_length=10)
    

    def __str__(self):
        return self.name
    
    
 # Création Model Fournisseur



 # Création Model Produit



class Produit(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=False)
    price = models.PositiveIntegerField(unique=False)
    image = models.ImageField(upload_to='event_category/')
    stock = models.PositiveIntegerField()
    description = RichTextUploadingField()
    volume = models.DecimalField(max_digits=10000, decimal_places=2)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disponible', 'Disponible'),
        ('rupture', 'Rupture de stock'),
        ('endommagé', 'Endomagé'),
    )
    status = models.CharField(choices=status_choice, max_length=10, default='disponible')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-list')
    
    def created_updated(model, request):
        obj = model.objects.latest('pk') # type: ignore
        if obj.created_by is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        
        
class Fournisseur(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=8)
    ville = models.CharField(max_length=32)
    pays = models.CharField(max_length=32)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
         ('actif', 'Actif'),
        ('abandonné', 'Abandonné'),
        ('bloqué', 'Bloqué'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    
    def get_absolute_url(self):
        return reverse('event-wish-list')
        
class Livraison(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_category/')
    price = models.PositiveIntegerField(unique=False)
    quantite = models.PositiveIntegerField(unique=False)
    ville = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    location = LocationField()
    volume = models.DecimalField(max_digits=10000, decimal_places=1)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('en cours', 'En cours'),
        ('terminé', 'Terminé'),
        ('annuler', 'Annuler'),
    )
    status = models.CharField(choices=status_choice, max_length=10, default='en cours')

    def __str__(self):
        return self.quantite
    
    def get_absolute_url(self):
        return reverse('event-list')
    
    def create_updated(model, request):
        obj = model.objects.latest('pk') # type: ignore
        if obj.created_by is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        
    @property
    def get_total(self):
        totale = self.quantite * self.price    # type: ignore
        return totale

class EventImage(models.Model):
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_image/')
    
    
    
    
    
    
class Commande(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE)
    nbre_cmd = models.PositiveIntegerField()
    prix = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10000, decimal_places=2)
    date_cmd = models.DateField(auto_now_add=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('livrée', 'Livrée'),
        ('en cours', 'En cours'),
        ('annulée', 'Annulée'),
    )
    status = models.CharField(choices=status_choice, max_length=10)




#A supprimer




































































class EventAgenda(models.Model):
    event = models.ForeignKey(Produit, on_delete=models.CASCADE)
    session_name = models.CharField(max_length=120)
    speaker_name = models.CharField(max_length=120)
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue_name = models.CharField(max_length=255)


class EventJobCategoryLinking(models.Model):
    event = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return str(self.event)


class EventMember(models.Model):
    event = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    attend_status_choice = (
        ('waiting', 'Waiting'),
        ('attending', 'Attending'),
        ('completed', 'Completed'),
        ('absent', 'Absent'),
        ('cancelled', 'Cancelled'),
    )
    attend_status = models.CharField(choices=attend_status_choice, max_length=10)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)


    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('join-event-list')
    
    
# Le model Fournisseur



    
    
    
    


class UserCoin(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    CHOICE_GAIN_TYPE = (
        ('event', 'Event'),
        ('others', 'Others'),
    )
    gain_type = models.CharField(max_length=6, choices=CHOICE_GAIN_TYPE)
    gain_coin = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('user-mark')









