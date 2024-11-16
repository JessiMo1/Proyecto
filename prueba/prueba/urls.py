from django.contrib import admin
from django.urls import path, include


from generales.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('generales.urls')),
]
