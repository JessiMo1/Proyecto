from django.urls import path
from catalogos.views import estudianteRead,estudianteCreate, estudianteUpdate, estudianteDelete
from catalogos.views import profesorRead,profesorCreate, profesorUpdate, profesorDelete
from catalogos.views import claseRead,claseCreate
from catalogos.views import aulaRead,aulaCreate,asistencia_lista
from . import views

urlpatterns = [
    path('reporte/pdf/', views.generar_reporte_pdf, name='reporte_pdf'),
    path('estudiante/read/', estudianteRead, name='estudianteRead'),
    path('estudiante/create', estudianteCreate, name='estudianteCreate'),
    path('estudiante/update/<int:id>/', estudianteUpdate, name='estudianteUpdate'),
    path('estudiante/delete/<int:id>/', estudianteDelete, name='estudianteDelete'),

    path('profesor/read/', profesorRead, name='profesorRead'),
    path('profesor/create', profesorCreate, name='profesorCreate'),
    path('profesor/update/<int:id>/', profesorUpdate, name='profesorUpdate'),
    path('profesor/delete/<int:id>/', profesorDelete, name='profesorDelete'),

    path('clase/read/', claseRead, name='claseRead'),
    path('clase/create', claseCreate, name='claseCreate'),

    path('aula/read/', aulaRead, name='aulaRead'),
    path('aula/create', aulaCreate, name='aulaCreate'),

    path('asistencia/lista/', asistencia_lista, name='asistencia_lista'),
]