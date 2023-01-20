from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appFunctional.views import *


urlpatterns = [
    path('', include('appFunctional.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
