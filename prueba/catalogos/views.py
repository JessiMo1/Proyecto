from django.shortcuts import render,redirect
from catalogos.models import  Estudiante, Clase, Aula, Profesor,Asistencia
from catalogos.forms import   EstudianteForm,ProfesorForm,ClaseForm,AulaForm
# Create your views here.
def estudianteRead(request):
    # Recuperar parámetros de búsqueda y filtros
    query = request.GET.get('q', '').strip()
    semestre = request.GET.get('semestre')
    clase_id = request.GET.get('clase')

    # Obtener todos los estudiantes inicialmente
    estudiantes = Estudiante.objects.all()
    
    # Filtrar por nombre si se proporciona
    if query:
        estudiantes = estudiantes.filter(nombre__icontains=query)
    
    # Filtrar por semestre si se proporciona
    if semestre:
        estudiantes = estudiantes.filter(semestre=semestre)
    
    # Filtrar por materia si se proporciona
    if clase_id:
        estudiantes = estudiantes.filter(clase_id=clase_id)
    
    # Obtener las materias para el filtro en el template
    clases = Clase.objects.all()

    # Crear el rango de semestres, en este caso de 1 a 10
    semestres = range(1, 11)

    # Pasar los datos al contexto
    data = {
        'estudiantes': estudiantes,
        'clases': clases,
        'query': query,
        'semestre': semestre,
        'clase_id': clase_id,
        'semestres': semestres,  # Se pasa el rango de semestres a la plantilla
    }
    return render(request, 'estudianteRead.html', data)



#Insercion de datos
def estudianteCreate(request): 
    if request.method == 'POST':  # se requiere guardar el formulario lleno
        form = EstudianteForm(request.POST)  # se envía el formulario con el método POST
        if form.is_valid():  # si el formulario está lleno correctamente
            form.save()  # guarda un registro en la tabla de base de datos
            return redirect('estudianteRead')  # redirige al listado de carrera
    else:
        form = EstudianteForm()  # se pinta el formulario al ingresar con una solicitud GET

    return render(request, 'estudianteCreate.html', {'form': form})

#Update
def estudianteUpdate(request, id):
    estudiante =Estudiante.objects.get(id=id)
    if request.method == 'GET':
        form =EstudianteForm(instance= estudiante)
    else:
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
        return redirect('estudianteRead')
    return render(request,'estudianteCreate.html',{'form':form})

#Eliminacion de un dato 
def estudianteDelete(request, id):
    estudiante = Estudiante.objects.get(id=id)  # Obtiene la instancia específica de Profesor
    if request.method == 'POST':
        estudiante.delete()  # Llama a delete() en la instancia específica
        return redirect('estudianteRead')
    return render(request, 'estudianteDelete.html', {'estudiante': estudiante})


def profesorRead(request):
    # Recuperar parámetros de búsqueda y filtros
    query = request.GET.get('q', '').strip()  # Filtro por nombre o clave
    aula_id = request.GET.get('aula')  # Filtro por aula
    clase_id = request.GET.get('clase')  # Filtro por materia

    # Obtener todos los profesores inicialmente
    profesores = Profesor.objects.all()

    # Filtrar por nombre o clave si se proporciona
    if query:
        profesores = profesores.filter(nombre__icontains=query) | profesores.filter(clave__icontains=query)
    
    # Filtrar por aula si se proporciona
    if aula_id:
        profesores = profesores.filter(aula_id=aula_id)
    
    # Filtrar por materia si se proporciona
    if clase_id:
        profesores = profesores.filter(clase_id=clase_id)

    # Obtener los objetos de Aula para el filtro en el template
    aulas = Aula.objects.all()

    # Obtener las materias para el filtro en el template
    clases = Clase.objects.all()

    # Pasar los datos al contexto
    data = {
        'profesores': profesores,
        'aulas': aulas,  # Se pasa la lista de aulas al contexto
        'clases': clases,  # Se pasa la lista de materias al contexto
        'query': query,
        'aula_id': aula_id,
        'clase_id': clase_id,
    }
    
    return render(request, 'profesorRead.html', data)

def profesorCreate(request): 
    if request.method == 'POST':  # se requiere guardar el formulario lleno
        form = ProfesorForm(request.POST)  # se envía el formulario con el método POST
        if form.is_valid():  # si el formulario está lleno correctamente
            form.save()  # guarda un registro en la tabla de base de datos
            return redirect('profesorRead')  # redirige al listado de carrera
    else:
        form = ProfesorForm()  # se pinta el formulario al ingresar con una solicitud GET

    return render(request, 'profesorCreate.html', {'form': form})


def profesorUpdate(request, id):
    profesor =Profesor.objects.get(id=id)
    if request.method == 'GET':
        form =ProfesorForm(instance= profesor)
    else:
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
        return redirect('profesorRead')
    return render(request,'profesorCreate.html',{'form':form})

def profesorDelete(request, id):
    profesor = Profesor.objects.get(id=id)  # Obtiene la instancia específica de Profesor
    if request.method == 'POST':
        profesor.delete()  # Llama a delete() en la instancia específica
        return redirect('profesorRead')
    return render(request, 'profesorDelete.html', {'profesor': profesor})

def claseRead(request):
    clases = Clase.objects.all()
    data= {'clases' : clases}
    return render (request, 'claseRead.html', data)

def  claseCreate(request): 
    if request.method == 'POST':  # se requiere guardar el formulario lleno
        form = ClaseForm(request.POST)  # se envía el formulario con el método POST
        if form.is_valid():  # si el formulario está lleno correctamente
            form.save()  # guarda un registro en la tabla de base de datos
            return redirect('claseRead')  # redirige al listado de carrera
    else:
        form = ClaseForm()  # se pinta el formulario al ingresar con una solicitud GET

    return render(request, 'claseCreate.html', {'form': form})

def aulaRead(request):
    aulas = Aula.objects.all()
    data= {'aulas' : aulas}
    return render (request, 'aulaRead.html', data)

#insercion de datos de aula
def aulaCreate(request): 
    if request.method == 'POST':  # se requiere guardar el formulario lleno
        form = AulaForm(request.POST)  # se envía el formulario con el método POST
        if form.is_valid():  # si el formulario está lleno correctamente
            form.save()  # guarda un registro en la tabla de base de datos
            return redirect('aulaRead')  # redirige al listado de carrera
    else:
        form = AulaForm()  # se pinta el formulario al ingresar con una solicitud GET

    return render(request, 'aulaCreate.html', {'form': form})

def asistencia_lista(request):
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    clases = Clase.objects.all()
    aulas = Aula.objects.all()

    # Filtros
    nombre_profesor = request.GET.get('nombre_profesor', '')
    aula_id = request.GET.get('aula', '')
    clase_id = request.GET.get('clase', '')

    if nombre_profesor:
        profesores = profesores.filter(nombre__icontains=nombre_profesor)

    if aula_id:
        profesores = profesores.filter(aula_id=aula_id)

    if clase_id:
        asistencias = Asistencia.objects.filter(clase_id=clase_id)
    else:
        asistencias = Asistencia.objects.all()

    # Pasar los datos al template
    return render(request, 'asistencia_lista.html', {
        'asistencias': asistencias,
        'estudiantes': estudiantes,
        'profesores': profesores,
        'clases': clases,
        'aulas': aulas,
        'nombre_profesor': nombre_profesor,
        'aula_id': aula_id,
        'clase_id': clase_id,
    })