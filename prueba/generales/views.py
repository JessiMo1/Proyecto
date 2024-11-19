from django.shortcuts import render,redirect
from generales.forms import logForm, usuarioForm
from django.contrib.auth import authenticate, login, logout
from generales.models import Usuario
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
    
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        form = logForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=request.POST['usunom'],
                                password=request.POST['contraseña'])
            if user is None:
                return render(request, 'login.html', {'form': form, 'error': 'La contraseña o usuario son incorrectos'})
            else:
                login(request, user)
                return redirect('home')
    else:
        form = logForm()
    return render(request, 'login.html', {'form': form})


def usuarioCreate(request):
    if request.method == 'POST':
            form = usuarioForm(request.POST)
            if form.is_valid():
                # Validación de las contraseñas
                if request.POST['contraseña'] == request.POST['contraseña2']:
                    try:
                        # Crear un nuevo usuario con los datos del formulario
                        usuario = Usuario.objects.create(
                            nombre=request.POST['nombre'],
                            usunom=request.POST['usunom'],
                            email=request.POST['email'],
                            password=request.POST['contraseña'],
                            genero = request.POST['genero'],
                            roles='usuario',  # Puedes ajustar esto según el rol por defecto
                            
                        )
                        usuario.save()  # Guardar el usuario en la base de datos
                        
                        # Realizar el login automáticamente con el nuevo usuario
                        login(request, usuario)
                        
                        # Redirigir al inicio o a la página que desees
                        return redirect('home')  # Cambia 'inicio' al nombre de la vista a la que quieras redirigir
                    except IntegrityError:
                        # Si el usuario ya existe, muestra un error
                        return render(request, 'gestionACreate.html', {
                            'form': form,
                            'error': 'El usuario ya existe'
                        })
                else:
                    # Si las contraseñas no coinciden, muestra un mensaje de error
                    return render(request, 'createUsuarios.html', {
                        'form': form,
                        'error': 'Las contraseñas no coinciden'
                    })
            else:
                form = usuarioForm()  # Si no es un POST, muestra el formulario vacío
        
    return render(request, 'gestionACreate.html', {'form': form})



def logout(request):
    return render(request,'logout.html')

def tables(request):
    return render(request,'tables.html')

def gestionARead(request):
    gestiona = Usuario.objects.all()
    data= {'gestiona' : gestiona}
    return render (request, 'gestionARead.html', data)

def gestionACreate(request): 
    if request.method == 'POST':  # se requiere guardar el formulario lleno
        form = usuarioForm(request.POST)  # se envía el formulario con el método POST
        if form.is_valid():  # si el formulario está lleno correctamente
            form.save()  # guarda un registro en la tabla de base de datos
            return redirect('gestionARead')  # redirige al listado de gestion
        
    else:
        form = usuarioForm()  # se pinta el formulario al ingresar con una solicitud GET

    return render(request, 'gestionACreate.html', {'form': form})

#update
def gestionAUpdate(request, id):
    gestiona =Usuario.objects.get(id=id)
    if request.method == 'GET':
        form =usuarioForm(instance= gestiona)
    else:
        form = usuarioForm(request.POST, instance=gestiona)
        if form.is_valid():
            form.save()
        return redirect('gestionARead')
    return render(request,'gestionACreate.html',{'form':form})

def gestionADelete(request, id):
    gestiona = Usuario.objects.get(id=id)  # Obtiene la instancia específica de Profesor
    if request.method == 'POST':
        gestiona.delete()  # Llama a delete() en la instancia específica
        return redirect('gestionARead')
    return render(request, 'gestionADelete.html', {'gestiona': gestiona})