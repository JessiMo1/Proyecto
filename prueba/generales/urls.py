from django.urls import path

from generales.views import login
from generales.views import logout
from generales.views import home

urlpatterns = [
    path('home/', home, name = 'home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]