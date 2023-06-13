from django.urls import path

from .views import (
    AbsenseLivreurList,
    AddLivreurCreate,
    CategoryList,
    CategoryCreate,
    CategoryUpdate,
    CategoryDelete,
    ClientDetail,
    CreateUserMark,
    LivraisonCreateView,
    LivraisonDelete,
    LivraisonDetail,
    LivraisonList,
    LivraisonUpdate,
    LivreurDelete,
    LivreurDetail,
    LivreurList,
    LivreurUpdate,
    LivreurUserList,
    ProductCreateView,
    FournisseurDetail,
    ProductList,
    ProductUpdate,
    ProductDetail,
    ProductDelete,
    AddClientCreate,
    ClientList,
    ClientUpdate,
    ClientDelete,
    FournisseurCreate,
    FournisseurDelete,
    UpdateClientStatus,
    UpdateFournisseurStatus,
    UpdateLivreurStatus,
    UpdateProductStatus,
    CompleteProductList,
    AbsenseClientList,
    ClientUserList,
    UpdateLivraisonStatus,
    UserMarkList,
    search_event_category,
    search_event,
    create_event,
    FournisseurList,
    FournisseurUpdate,
) 

urlpatterns = [
    
    #url des catégories des produits

    path('category-list/', CategoryList.as_view(), name='event-category-list'),
    path('create-category/', CategoryCreate.as_view(), name='create-event-category'),
    path('category/<int:pk>/edit/', CategoryUpdate.as_view(), name='edit-event-category'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='delete-event-category'),
    
    #url des  produits

    path('event-create/', ProductCreateView.as_view(), name='event-create'),
    path('event-list/', ProductList.as_view(), name='event-list'),
    path('event/<int:pk>/edit/', ProductUpdate.as_view(), name='event-edit'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='event-detail'),
    path('delete/<int:pk>', ProductDelete.as_view(), name='event-delete'),
    path('update-status/<int:pk>/event/', UpdateProductStatus.as_view(), name='update-event-status'),
    
    
    #url des  livraisons

    path('create_livraison/', LivraisonCreateView.as_view(), name='create_livraison'),
    path('livraison_list/', LivraisonList.as_view(), name='livraison_list'),
    path('livraison/<int:pk>/edit/', LivraisonUpdate.as_view(), name='edit_livraison'),
    path('detail/<int:pk>/livraison', LivraisonDetail.as_view(), name='livraison_detail'),
    path('delete/<int:pk>/livraison', LivraisonDelete.as_view(), name='delete_livraison'),
    path('livraisonStatus/<int:pk>/livraison/', UpdateLivraisonStatus.as_view(), name='livraisonStatus'),

    
    #url  des Clients
    
    path('add-event-member/', AddClientCreate.as_view(), name='add-event-member'),
    path('join-event-list/', ClientList.as_view(), name='join-event-list'),
    path('editerClient/<int:pk>/update/', ClientUpdate.as_view(), name='editerClient'),
    path('clientDetail/<int:pk>/Detail/', ClientDetail.as_view(), name='clientDetail'),
    path('event-member/<int:pk>/remove/', ClientDelete.as_view(), name='remove-event-member'),
    path('complete-event-user/', ClientUserList.as_view(), name='complete-event-user'),
    path('absense-user/', AbsenseClientList.as_view(), name='absense-user'),
    path('editerStatus/<int:pk>/client/', UpdateClientStatus.as_view(), name='editerStatusClient'),


    #url  des Fournisseurs
     
    path('event-wish-list/', FournisseurList.as_view(), name='event-wish-list'),
    path('liste_fournisseur/', FournisseurList.as_view(), name='liste_fournisseur'),
    path('add-event-wish-user/', FournisseurCreate.as_view(), name='add-event-wish-user'),
    path('event-user-wish/<int:pk>/remove/', FournisseurDelete.as_view(), name='remove-event-user-wish'),
    path('detailFournisseur/<int:pk>/Detail/', FournisseurDetail.as_view(), name='detailFournisseur'),
    path('editeFournisseur/<int:pk>/editer/', FournisseurUpdate.as_view(), name='editeFournisseur'),
    path('editerStatus/<int:pk>/fournisseur/', UpdateFournisseurStatus.as_view(), name='editerStatusfourn'),
    
    
    
    #url  des Livreurs
    
    path('ajoutLivreur/', AddLivreurCreate.as_view(), name='ajoutLivreur'),
    path('listeLivreur/', LivreurList.as_view(), name='listeLivreur'),
    path('editerLivreur/<int:pk>/update/', LivreurUpdate.as_view(), name='editerLivreur'),
    path('detailLivreur/<int:pk>/Detail/', LivreurDetail.as_view(), name='detailLivreur'),
    path('removeLivreur/<int:pk>/remove/', LivreurDelete.as_view(), name='removeLivreur'),
    path('livreur/', LivreurUserList.as_view(), name='complete-event-user'),
    path('absense_livreur/', AbsenseLivreurList.as_view(), name='absense-livreur'),
    path('editerStatus/<int:pk>/livreur/', UpdateLivreurStatus.as_view(), name='editerStatus'),



    path('complete-event/', CompleteProductList.as_view(), name='complete-event'),
    path('create-user-mark/', CreateUserMark.as_view(), name='create-user-mark'),
    path('user-mark/', UserMarkList.as_view(), name='user-mark'),
    path('search_category/', search_event_category, name='search-event-category'),
    path('search_event/', search_event, name='search-event'),
    path('create/', create_event, name='create'),
]