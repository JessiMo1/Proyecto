from django.db import models

# Modelo que representa a un usuario en el sistema
class Usuario(models.Model):
    # El nombre completo del usuario, se permite que sea nulo o vacío y debe ser único
    nombre = models.CharField(max_length=150, null=True, blank=True, unique=True)

    # El nombre de usuario (usado para login o identificación), se permite que sea nulo o vacío y debe ser único
    usunom = models.CharField(max_length=150, null=True, blank=True, unique=True)

    # El correo electrónico del usuario, debe ser único
    email = models.EmailField(unique=True)

    # La contraseña del usuario, se limita a un máximo de 128 caracteres
    # Se especifica un texto de ayuda para indicar la longitud máxima
    contraseña = models.CharField(max_length=128, help_text='Máximo 128 caracteres')  # Compatible con Django

    # Campo de fecha y hora de creación del registro, se establece automáticamente al crear el objeto
    created = models.DateTimeField(auto_now_add=True)

    # Campo de fecha y hora de la última actualización del registro, se actualiza automáticamente
    updated = models.DateTimeField(auto_now=True)

    # Definición de opciones de rol del usuario (usuario normal o administrador)
    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    # Campo para definir el rol del usuario, con un valor por defecto de 'usuario'
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

    # Definición de opciones de género (Hombre, Mujer, Otro, Prefiero no decirlo)
    OPCIONES_GENERO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
        ('prefiero_no_decirlo', 'Prefiero no decirlo'),
    ]
    # Campo para seleccionar el género del usuario, con un valor por defecto de 'Prefiero no decirlo'
    genero = models.CharField(max_length=20, choices=OPCIONES_GENERO, default='prefiero_no_decirlo')

    # Metadatos del modelo
    class Meta:
        verbose_name = 'usuario'  # Nombre singular para el modelo
        verbose_name_plural = 'usuarios'  # Nombre plural para el modelo

    # Método para representar al usuario en formato de cadena (se muestra nombre y rol)
    def __str__(self):
        return f"{self.nombre} ({self.roles})"
