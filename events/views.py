from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    Categorie,
    Livreur,
    Produit,
    Livraison,
    Client,
    Fournisseur,
    UserCoin,

)
from .forms import ProductForm, ProductImageForm, EventAgendaForm, CreateMultiForm, LivraisonMultiForm


#Début de la vue des catégories des produits

class CategoryList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Categorie
    template_name = 'events/event_category.html'
    context_object_name = 'event_category'


class CategoryCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Categorie
    fields = ['name', 'code','status']
    template_name = 'events/create_event_category.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Categorie
    fields = ['name', 'code','status']
    template_name = 'events/edit_event_category.html'


class CategoryDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Categorie
    template_name = 'events/event_category_delete.html'
    success_url = reverse_lazy('event-category-list')

@login_required(login_url='login')
def create_event(request):
    event_form = ProductForm()
    event_image_form = ProductImageForm()
    event_agenda_form = EventAgendaForm()
    catg = Categorie.objects.all()
    if request.method == 'POST':
        event_form = ProductForm(request.POST)
        event_image_form = ProductImageForm(request.POST, request.FILES)
        if event_form.is_valid() and event_image_form.is_valid() and event_agenda_form.is_valid():
            ef = event_form.save()
            created_updated(Produit, request) # type: ignore
            event_image_form.save(commit=False)
            event_image_form.event_form = ef # type: ignore
            event_image_form.save()
            return redirect('event-list')
    context = {
        'form': event_form,
        'form_1': event_image_form,
        'ctg': catg
    }
    return render(request, 'events/create.html', context)
@login_required(login_url='login')
def search_event_category(request):
    if request.method == 'POST':
       data = request.POST['search']
       event_category = Categorie.objects.filter(name__icontains=data)
       context = {
           'event_category': event_category
       }
       return render(request, 'events/event_category.html', context)
    return render(request, 'events/event_category.html')


#Début de la vue des produits


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = CreateMultiForm # type: ignore
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event-list')

    def form_valid(self, form):
        print(form['event'])
        evt = form['event'].save(commit=False) # type: ignore
      

        return super().form_valid(form)




class ProductList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Produit
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class ProductUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Produit
    fields = ['category', 'name', 'price', 'stock','image', 'description', 'volume', 'status']
    template_name = 'events/edit_event.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Produit
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class ProductDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Produit
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event-list')


class CompleteProductList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Produit
    template_name = 'events/complete_event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Produit.objects.filter(status='completed')
    
@login_required(login_url='login')
def search_event(request):
    if request.method == 'POST':
       data = request.POST['search']
       events = Produit.objects.filter(name__icontains=data)
       context = {
           'events': events
       }
       return render(request, 'events/event_list.html', context)
    return render(request, 'events/event_list.html')


class UpdateProductStatus(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Produit
    fields = ['status']
    template_name = 'events/update_event_status.html'
    

#Début de la vue de la livraison


class LivraisonCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    form_class = LivraisonMultiForm # type: ignore
    template_name = 'events/create_livraison.html'
    success_url = reverse_lazy('livraison_list')

    def form_valid(self, form):
        evt = form['event'].save(commit=False) # type: ignore
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['ctg'] = Categorie.objects.all()
        return context


class LivraisonList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Livraison
    template_name = 'events/livraison_list.html'
    context_object_name = 'livraisons'


class LivraisonUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Livraison
    fields = ['produit','image', 'price','quantite','ville', 'start_date', 'location','volume', 'status']
    template_name = 'events/edit_livraison.html'
    success_url = reverse_lazy('livraison_list')


class LivraisonDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Livraison
    template_name = 'events/livraison_detail.html'
    context_object_name = 'livraisons'
    #success_url = reverse_lazy('livraison_list')


class LivraisonDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Livraison
    template_name = 'events/delete_livraison.html'
    success_url = reverse_lazy('livraison_list')
    
class UpdateLivraisonStatus(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Livraison
    fields = ['status']
    template_name = 'events/livraisonStatus.html'
    success_url = reverse_lazy('livraison_list')

#Début de la vue des clients


class AddClientCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model=Client
    fields = ['name', 'email', 'telephone', 'address', 'sexe' ,'city','status']
    template_name = 'events/add_event_member.html'
    success_url = reverse_lazy('join-event-list')


    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class ClientList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Client
    template_name = 'events/joinevent_list.html'
    context_object_name = 'eventmember'
    
    
class ClientUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Client
    fields = ['name', 'email', 'telephone', 'address', 'sexe' ,'city','status']
    template_name = 'events/editerClient.html'

    def dispatch(self, request, *args, **kwargs):
        if 'pk' not in self.kwargs:
            return redirect('join-event-list')
        return super().dispatch(request, *args, **kwargs)


class ClientDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model=Client
    template_name = 'events/remove_event_member.html'
    success_url = reverse_lazy('join-event-list')
    
   
class ClientUserList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Client
    template_name = 'events/complete_event_user_list.html'
    context_object_name = 'completeuser'

    def get_queryset(self):
        return  Client.objects.filter(attend_status='completed')


class AbsenseClientList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Client
    template_name = 'events/absense_user_list.html'
    context_object_name = 'absenseuser'

    def get_queryset(self):
        return Client.objects.filter(attend_status='absent')

class ClientDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Client
    template_name = 'events/clientDetail.html'
    context_object_name = 'client'
    
class UpdateClientStatus(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Client
    fields = ['status']
    template_name = 'events/editerStatusClient.html'
    success_url = reverse_lazy('join-event-list')
    
    

#Début de la vue des Fournisseurs

class FournisseurCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model=Fournisseur
    fields = ['produit','nom', 'telephone','ville', 'pays','status']

    template_name = 'events/add_event_user_wish.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)

  
    

class FournisseurList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Fournisseur
    template_name = 'events/liste_fournisseur.html'
    context_object_name = 'eventwish'
   


class FournisseurDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model=Fournisseur
    template_name = 'events/remove_event_user_wish.html'
    success_url = reverse_lazy('event-wish-list')


class FournisseurUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Fournisseur
    fields = ['nom', 'telephone','ville', 'pays','status']
    template_name = 'events/editeFournisseur.html'

    def dispatch(self, request, *args, **kwargs):
        if 'pk' not in self.kwargs:
            return redirect('liste_fournisseur')
        return super().dispatch(request, *args, **kwargs)

class FournisseurDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Fournisseur
    template_name = 'events/detailFournisseur.html'
    context_object_name = 'fournisseur'
    
    
class UpdateFournisseurStatus(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Fournisseur
    fields = ['status']
    template_name = 'events/editerStatusfourn.html'
    success_url = reverse_lazy('liste_fournisseur')





# Fin de la vue des Fournisseurs



#Début de la vue des Livreurs




class AddLivreurCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model=Livreur
    fields = ['name', 'email', 'telephone', 'addresse', 'sexe','status']
    template_name = 'events/ajoutClient.html'
    success_url = reverse_lazy('listeLivreur')


    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class LivreurList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Livreur
    template_name = 'events/listeLivreur.html'
    context_object_name = 'livreurs'
    
    
class LivreurUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Livreur
    fields = ['name', 'email', 'telephone', 'addresse', 'sexe' ,'status']
    template_name = 'events/editerLivreur.html'

    def dispatch(self, request, *args, **kwargs):
        if 'pk' not in self.kwargs:
            return redirect('listeLivreur')
        return super().dispatch(request, *args, **kwargs)


class LivreurDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model=Livreur
    template_name = 'events/removeLivreur.html'
    success_url = reverse_lazy('listeLivreur')
    
   
class LivreurUserList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Livreur
    template_name = 'events/complete_event_user_list.html'
    context_object_name = 'completeuser'

    def get_queryset(self):
        return  Livreur.objects.filter(attend_status='completed')


class AbsenseLivreurList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model=Livreur
    template_name = 'events/absense_user_list.html'
    context_object_name = 'absenseuser'

    def get_queryset(self):
        return Livreur.objects.filter(attend_status='absent')

class LivreurDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Livreur
    template_name = 'events/detailLivreur.html'
    context_object_name = 'livreurs'
    
    
class UpdateLivreurStatus(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Livreur
    fields = ['status']
    template_name = 'events/editerStatus.html'
    success_url = reverse_lazy('listeLivreur')








class CreateUserMark(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = UserCoin
    fields = ['user', 'gain_type', 'gain_coin', 'status']
    template_name = 'events/create_user_mark.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class UserMarkList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = UserCoin
    template_name = 'events/user_mark_list.html'
    context_object_name = 'usermark'





