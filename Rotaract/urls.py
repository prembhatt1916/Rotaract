from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    
]

#if settting.DEBUG:
    #urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



