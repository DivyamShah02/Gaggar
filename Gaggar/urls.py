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
    path(route='rpet/', view=rpet, name='rpet'),
    path(route='about/', view=about, name='about'),
    path(route='contact/', view=contact, name='contact'),
    
    path(route='terms_conds/', view=terms_conds, name='terms_conds'),
    path(route='privacy_policy/', view=privacy_policy, name='privacy_policy'),
    path(route='cookies_policy/', view=cookies_policy, name='cookies_policy'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
