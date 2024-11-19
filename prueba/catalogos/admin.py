from django.contrib import admin
from catalogos.models import Estudiante, Clase, Profesor, Aula, Asistencia
# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Clase)
admin.site.register(Profesor)
admin.site.register(Aula)
admin.site.register(Asistencia)