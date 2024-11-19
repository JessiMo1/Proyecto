from django.contrib import admin
from django.urls import path, include


from generales.views import login, logout, home, tables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('generales.urls')),
     path('', include ('catalogos.urls')),
]

