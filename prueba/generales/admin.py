from django.contrib import admin

# Register your models here.
from generales.models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre')
    search_fields = ['nombre']
    readonly_fields = ('created', 'updated')
    filter_horizontal= ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Usuario, UsuarioAdmin)