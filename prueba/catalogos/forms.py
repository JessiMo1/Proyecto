from django import forms
from catalogos.models import  Estudiante, Clase, Aula, Profesor

class ClaseForm(forms.ModelForm):
        class Meta:#Son las propiedades que utilizara el formulario
                model = Clase
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs) #inicializacion automatica
                for field in iter(self.fields):
                       self.fields[field].widget.attrs.update({'class':'form-control'})

class EstudianteForm(forms.ModelForm):
        class Meta:#Son las propiedades que utilizara el formulario
                model = Estudiante
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs) #inicializacion automatica
                for field in iter(self.fields):
                       self.fields[field].widget.attrs.update({'class':'form-control'})

class ProfesorForm(forms.ModelForm):
        class Meta:#Son las propiedades que utilizara el formulario
                model = Profesor
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs) #inicializacion automatica
                for field in iter(self.fields):
                       self.fields[field].widget.attrs.update({'class':'form-control'})

class AulaForm(forms.ModelForm):
        class Meta:#Son las propiedades que utilizara el formulario
                model = Aula
                fields = '__all__'
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs) #inicializacion automatica
                for field in iter(self.fields):
                       self.fields[field].widget.attrs.update({'class':'form-control'})