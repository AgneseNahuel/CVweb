from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('python', Python, name='Python'),
    path('html/', Html, name='html'),
    path('css/', Css, name='css'),
    path('leerMasPython/<int:pk>', leerMasPython.as_view(), name='leerMasPython'),
    path('leerMasHtml/<int:pk>', leerMasHtml.as_view(), name='leerMasHtml'),
    path('leerMasCss/<int:pk>', leerMasCss.as_view(), name='leerMasCss'),
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)