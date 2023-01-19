from django.urls import path
from .views import *

urlpatterns = [
    path('', layout, name='layout'),
    
]