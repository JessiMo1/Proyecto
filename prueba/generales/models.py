from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=150, null=True, blank=True, unique=True)
    usunom = models.CharField(max_length=150, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128, help_text='Máximo 128 caracteres')  # Compatible con Django
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

    OPCIONES_GENERO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
        ('prefiero_no_decirlo', 'Prefiero no decirlo'),
    ]
    genero = models.CharField(max_length=20, choices=OPCIONES_GENERO, default='prefiero_no_decirlo')

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return f"{self.nombre} ({self.roles})"
