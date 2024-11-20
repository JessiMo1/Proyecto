from django.db import models

# Modelo Estudiante
class Estudiante(models.Model):
    # Atributos del modelo Estudiante
    no_control = models.CharField(max_length=10, unique=True)  # Identificador único del estudiante
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Nombre del estudiante (opcional)
    correo = models.EmailField(unique=True)  # Correo electrónico único del estudiante
    credencial = models.CharField(max_length=20, unique=True)  # Número de credencial único
    genero = models.CharField(  # Género del estudiante con opciones predefinidas
        max_length=20,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No especificado', 'No especificado')
        ],
        default='No especificado'
    )
    semestre = models.IntegerField(default=5)  # Semestre actual del estudiante (por defecto 5)
    clase = models.ForeignKey(  # Relación con el modelo Clase
        'Clase',
        on_delete=models.CASCADE,  # Elimina al estudiante si se elimina su clase asociada
        related_name='estudiantes'  # Nombre para acceder a los estudiantes desde una clase
    )

    # Configuración del modelo
    class Meta:
        verbose_name = "Estudiante"  # Nombre en singular
        verbose_name_plural = "Estudiantes"  # Nombre en plural

    # Representación en formato string
    def __str__(self):
        return f"{self.no_control} - {self.nombre}"


# Modelo Clase
class Clase(models.Model):
    # Atributos del modelo Clase
    nombre = models.CharField(max_length=100, blank=True, null=True)  # Nombre de la clase (opcional)
    fechahora = models.DateTimeField(auto_now_add=True, null=True)  # Fecha y hora de creación automática
    aula = models.ForeignKey(  # Relación con el modelo Aula
        'Aula',
        on_delete=models.CASCADE,  # Elimina la clase si el aula asociada se elimina
        null=True  # Puede no estar relacionado con un aula
    )

    # Representación en formato string
    def __str__(self):
        return "{0}".format(self.nombre)


# Modelo Profesor
class Profesor(models.Model):
    # Atributos del modelo Profesor
    clave = models.CharField(max_length=10, unique=True)  # Identificador único del profesor
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Nombre del profesor (opcional)
    correo = models.EmailField(unique=True)  # Correo electrónico único del profesor
    huella_dactilar = models.CharField(max_length=255, unique=True)  # Identificador biométrico único
    departamento = models.CharField(max_length=150, blank=True, null=True)  # Departamento del profesor
    genero = models.CharField(  # Género del profesor con opciones predefinidas
        max_length=20,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No especificado', 'No especificado')
        ],
        default='No especificado'
    )
    aula = models.ForeignKey(  # Relación con el modelo Aula
        'Aula',
        on_delete=models.CASCADE,  # Elimina al profesor si el aula asociada se elimina
        null=True  # Puede no estar relacionado con un aula
    )
    clase = models.ManyToManyField(  # Relación de muchos a muchos con el modelo Clase
        'Clase',
        related_name='profesores',  # Nombre para acceder a los profesores desde una clase
        null=True  # Relación opcional
    )

    # Configuración del modelo
    class Meta:
        verbose_name = "Profesor"  # Nombre en singular
        verbose_name_plural = "Profesores"  # Nombre en plural

    # Representación en formato string
    def __str__(self):
        return f"{self.clave} - {self.nombre}"


# Modelo Aula
class Aula(models.Model):
    # Atributos del modelo Aula
    clave = models.CharField(max_length=20)  # Identificador único del aula
    nombre = models.CharField(max_length=10)  # Nombre del aula
    capacidad = models.IntegerField()  # Capacidad máxima del aula

    # Representación en formato string
    def __str__(self):
        return "{0} - {1}".format(self.clave, self.nombre)


# Modelo Asistencia
class Asistencia(models.Model):
    # Atributos del modelo Asistencia
    profesor = models.ForeignKey(  # Relación con el modelo Profesor
        Profesor,
        on_delete=models.CASCADE  # Elimina la asistencia si el profesor asociado se elimina
    )
    clase = models.ForeignKey(  # Relación con el modelo Clase
        Clase,
        on_delete=models.CASCADE  # Elimina la asistencia si la clase asociada se elimina
    )
    fecha = models.DateField()  # Fecha de la asistencia
    asistencia = models.BooleanField()  # Indica si asistió o no (True/False)

    # Representación en formato string
    def __str__(self):
        return f"{self.clase.nombre} - {self.fecha}"
