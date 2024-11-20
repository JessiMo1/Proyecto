# Importación de los módulos necesarios de Django
from django import forms
from generales.models import Usuario  # Importa el modelo 'Usuario' desde 'generales.models'

# Definición del formulario para el inicio de sesión (login)
class logForm(forms.Form):
    class Meta:
        model = Usuario  # Especifica que el formulario está basado en el modelo Usuario
        fields = [
            'usunom',  # El campo para el nombre de usuario
            'contraseña',  # El campo para la contraseña del usuario
        ]
        
        labels = {
            'usunom': 'Nombre del usuario',  # Etiqueta para el campo 'usunom'
            'contraseña': 'Contraseña del usuario'  # Etiqueta para el campo 'contraseña'
        }

    # Constructor del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base 'forms.Form'
        
        # Itera sobre todos los campos y les asigna una clase CSS 'form-control' para el estilo
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


# Definición del formulario para el registro o edición de un usuario
class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario  # Especifica que el formulario está basado en el modelo Usuario
        fields = [
            'nombre',  # El campo para el nombre del usuario
            'usunom',  # El campo para el nombre de usuario
            'email',  # El campo para el correo electrónico
            'contraseña',  # El campo para la contraseña
            'genero'  # El campo para seleccionar el género
        ]
        labels = {
            'nombre': 'Nombre',  # Etiqueta para el campo 'nombre'
            'usunom': 'Usuario',  # Etiqueta para el campo 'usunom'
            'email': 'Correo electrónico',  # Etiqueta para el campo 'email'
            'contraseña': 'Contraseña',  # Etiqueta para el campo 'contraseña'
            'genero': 'Elige su genero'  # Etiqueta para el campo 'genero'
        }

    # Constructor del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Llama al constructor de la clase base 'forms.ModelForm'
        
        # Itera sobre todos los campos y les asigna la clase CSS 'form-control' para el estilo
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
