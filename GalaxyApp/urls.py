
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('App.urls')),
    path('api/', include('App.api.urls')),
    
]
