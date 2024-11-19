from django.urls import path

from generales.views import login
from generales.views import logout
from generales.views import home, tables
from generales.views import gestionARead, gestionACreate, gestionAUpdate, gestionADelete
from . import views

urlpatterns = [
  
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),  # Ruta para la vista de inicio

    path('logout/', logout, name='logout'),
    path('tables/', logout, name='tables'),
    path('gestion-administradores/', gestionARead, name='gestionARead'),
    path('gestionA/create', gestionACreate, name='gestionACreate'),
    path('getionA/update/<int:id>/', gestionAUpdate, name='gestionAUpdate'),
    path('gestion/delete/<int:id>/', gestionADelete, name='gestionADelete'),
]