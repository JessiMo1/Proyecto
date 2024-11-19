from django import forms
from generales.models import Usuario

#class logForm(forms.Form):

class logForm(forms.Form):
    class Meta:
        model = Usuario
        fields=[
            'usunom',
            'contraseña',

        ]
        
        labels={
            'usunom':'Nombre del usuario',
            'contraseña': 'Contraseña del usuario'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields=[
            'nombre',
            'usunom',
            'email',
            'contraseña',
            'genero'
        ]
        labels={
            'nombre':'Nombre',
            'usunom':'Usuario',
            'email':'Correo electronico',
            'contraseña':'Contraseña',
            'genero':'Elige su genero'
        }
        '''
        widget={

        }
        '''
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})