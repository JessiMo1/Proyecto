from django import forms
from catalogos.models import Estudiante, Clase, Aula, Profesor

# Formulario para el modelo Clase
class ClaseForm(forms.ModelForm):
    class Meta:  # Configuración interna del formulario
        model = Clase  # Modelo al que está asociado el formulario
        fields = '__all__'  # Incluir todos los campos del modelo en el formulario

    def __init__(self, *args, **kwargs):
        # Inicialización del formulario
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base
        # Itera sobre todos los campos del formulario y agrega la clase CSS 'form-control'
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# Formulario para el modelo Estudiante
class EstudianteForm(forms.ModelForm):
    class Meta:  # Configuración interna del formulario
        model = Estudiante  # Modelo al que está asociado el formulario
        fields = '__all__'  # Incluir todos los campos del modelo en el formulario

    def __init__(self, *args, **kwargs):
        # Inicialización del formulario
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base
        # Itera sobre todos los campos del formulario y agrega la clase CSS 'form-control'
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# Formulario para el modelo Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:  # Configuración interna del formulario
        model = Profesor  # Modelo al que está asociado el formulario
        fields = '__all__'  # Incluir todos los campos del modelo en el formulario

    def __init__(self, *args, **kwargs):
        # Inicialización del formulario
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base
        # Itera sobre todos los campos del formulario y agrega la clase CSS 'form-control'
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# Formulario para el modelo Aula
class AulaForm(forms.ModelForm):
    class Meta:  # Configuración interna del formulario
        model = Aula  # Modelo al que está asociado el formulario
        fields = '__all__'  # Incluir todos los campos del modelo en el formulario

    def __init__(self, *args, **kwargs):
        # Inicialización del formulario
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base
        # Itera sobre todos los campos del formulario y agrega la clase CSS 'form-control'
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
