from django.shortcuts import render, redirect
from generales.forms import logForm, usuarioForm
from django.contrib.auth import authenticate, login, logout
from generales.models import Usuario
from django.contrib.auth.models import User
from django.db import IntegrityError

# Vista principal de la página de inicio
def home(request):
    return render(request, 'home.html')

# Vista para manejar el inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = logForm(request.POST)  # Se crea el formulario con los datos enviados por POST
        if form.is_valid():
            # Intentar autenticar al usuario con las credenciales proporcionadas
            user = authenticate(request, username=request.POST['usunom'], password=request.POST['contraseña'])
            if user is None:
                # Si el usuario no se encuentra o las credenciales son incorrectas
                return render(request, 'login.html', {'form': form, 'error': 'La contraseña o usuario son incorrectos'})
            else:
                # Si la autenticación es exitosa, iniciar sesión y redirigir al inicio
                login(request, user)
                return redirect('home')
    else:
        form = logForm()  # Si la solicitud no es POST, se muestra el formulario vacío
    return render(request, 'login.html', {'form': form})

# Vista para crear un nuevo usuario
def usuarioCreate(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)  # Crear el formulario con los datos del POST
        if form.is_valid():
            # Validación para asegurarse de que las contraseñas coinciden
            if request.POST['contraseña'] == request.POST['contraseña2']:
                try:
                    # Crear un nuevo usuario en la base de datos con los datos proporcionados
                    usuario = Usuario.objects.create(
                        nombre=request.POST['nombre'],
                        usunom=request.POST['usunom'],
                        email=request.POST['email'],
                        password=request.POST['contraseña'],
                        genero=request.POST['genero'],
                        roles='usuario',  # Rol predeterminado como 'usuario'
                    )
                    usuario.save()  # Guardar el usuario en la base de datos
                    
                    # Iniciar sesión automáticamente con el nuevo usuario
                    login(request, usuario)
                    
                    # Redirigir al inicio (o a la página que desees)
                    return redirect('home')
                except IntegrityError:
                    # Si ocurre un error de integridad (usuario ya existe), mostrar mensaje de error
                    return render(request, 'gestionACreate.html', {'form': form, 'error': 'El usuario ya existe'})
            else:
                # Si las contraseñas no coinciden, mostrar un mensaje de error
                return render(request, 'createUsuarios.html', {'form': form, 'error': 'Las contraseñas no coinciden'})
    else:
        form = usuarioForm()  # Si la solicitud no es POST, mostrar el formulario vacío
    return render(request, 'gestionACreate.html', {'form': form})

# Vista para cerrar sesión
def logout(request):
    return render(request, 'logout.html')

# Vista para mostrar una página con tablas (posiblemente de gestión)
def tables(request):
    return render(request, 'tables.html')

# Vista para leer y listar todos los usuarios (gestores)
def gestionARead(request):
    gestiona = Usuario.objects.all()  # Obtener todos los usuarios de la base de datos
    data = {'gestiona': gestiona}  # Pasar los usuarios al contexto
    return render(request, 'gestionARead.html', data)

# Vista para crear un nuevo usuario (gestor)
def gestionACreate(request): 
    if request.method == 'POST':  # Si la solicitud es POST, se guarda el formulario
        form = usuarioForm(request.POST)
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar el registro en la base de datos
            return redirect('gestionARead')  # Redirigir a la vista que muestra todos los usuarios
    else:
        form = usuarioForm()  # Si la solicitud es GET, mostrar el formulario vacío
    return render(request, 'gestionACreate.html', {'form': form})

# Vista para actualizar los datos de un usuario existente
def gestionAUpdate(request, id):
    gestiona = Usuario.objects.get(id=id)  # Obtener el usuario con el id proporcionado
    if request.method == 'GET':
        form = usuarioForm(instance=gestiona)  # Mostrar el formulario con los datos actuales del usuario
    else:
        form = usuarioForm(request.POST, instance=gestiona)  # Enviar el formulario con los datos modificados
        if form.is_valid():  # Si el formulario es válido
            form.save()  # Guardar los cambios en la base de datos
        return redirect('gestionARead')  # Redirigir a la vista de lista de usuarios
    return render(request, 'gestionACreate.html', {'form': form})

# Vista para eliminar un usuario
def gestionADelete(request, id):
    gestiona = Usuario.objects.get(id=id)  # Obtener el usuario a eliminar
    if request.method == 'POST':
        gestiona.delete()  # Eliminar el usuario de la base de datos
        return redirect('gestionARead')  # Redirigir a la vista de lista de usuarios
    return render(request, 'gestionADelete.html', {'gestiona': gestiona})  # Confirmar la eliminación en la vista
