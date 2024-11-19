from django.db import models


class Estudiante(models.Model):
    # Atributos
    no_control = models.CharField(max_length=10, unique=True)  # Control único para cada estudiante
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Nombre del estudiante
    correo = models.EmailField(unique=True)  # Correo electrónico único 
    credencial = models.CharField(max_length=20, unique=True)  # Número de credencial único
    genero = models.CharField(
        max_length=20, 
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No especificado', 'No especificado')
        ],
        default='No especificado'
    )
    semestre = models.IntegerField(default=5)  # Semestre en el que se encuentra
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE, related_name='estudiantes')  # related_name único)  # Relación personalizada
 

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

   # Métodos
    def __str__(self):
        return f"{self.no_control} - {self.nombre}"
    
class Clase(models.Model):
    # Atributos
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fechahora = models.DateTimeField(auto_now_add=True, null=True)  # Guarda la fecha y hora de creación
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE, null=True)  # Semestre en el que se encuentra
    prof= models.ManyToManyField('Profesor', related_name='clases', null=True) 
    # Métodos
    def __str__(self):
        return "{0}".format(self.nombre)
    
# Modelo Profesor
class Profesor(models.Model):
    # Atributos
    clave = models.CharField(max_length=10, unique=True)  # Clave única para cada profesor
    nombre = models.CharField(max_length=50, blank=True, null=True)  # Nombre del profesor
    correo = models.EmailField(unique=True)  # Correo electrónico único
    huella_dactilar = models.CharField(max_length=255, unique=True) 
    departamento = models.CharField(max_length=150, blank=True, null=True)
    genero = models.CharField(
        max_length=20,
        choices=[
            ('Masculino', 'Masculino'),
            ('Femenino', 'Femenino'),
            ('No especificado', 'No especificado')
        ],
        default='No especificado'
    )
    aula = models.ForeignKey('Aula', on_delete=models.CASCADE, null=True)  # Aula en la que enseña
    clase = models.ForeignKey('Clase', on_delete=models.CASCADE,null=True, related_name='profesores')  # related_name único)  # Cambiar related_name

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.clave} - {self.nombre}"




class Aula(models.Model):
    #Atributos
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    
    #Metodos
    def __str__(self):
        return "{0} - {1}".format(self.clave, self.nombre)
    
class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha = models.DateField()
    asistencia = models.BooleanField()  # True si asistió, False si no

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.clase.nombre} - {self.fecha}"



 