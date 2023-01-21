from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', Python, name='Python'),
    path('leerMas/<int:pk>', leerMas.as_view(), name='leerMas'),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)