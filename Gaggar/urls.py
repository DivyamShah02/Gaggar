from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path(route='', view=home, name='home'),
    path(route='products/', view=products, name='products'),
    path(route='about/', view=about, name='about'),
    path(route='contact/', view=contact, name='contact'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
