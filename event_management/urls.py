from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns #static,
from django.conf.urls.static import static


from .views import dashboard, login_page, logut_page
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('login/', login_page, name='login'),
    path('logout/', logut_page, name='logout'),
    path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)