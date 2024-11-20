from django.shortcuts import render,redirect
from catalogos.models import  Estudiante, Clase, Aula, Profesor,Asistencia
from catalogos.forms import   EstudianteForm,ProfesorForm,ClaseForm,AulaForm
from reportlab.lib.pagesizes import letter #type: ignore
from reportlab.pdfgen import canvas #type: ignore
from datetime import datetime
from django.http import HttpResponse

def generar_reporte_pdf(request):
    # Obtener parámetros de fecha desde la solicitud
    fecha_inicio = request.GET.get("fecha_inicio")
    fecha_fin = request.GET.get("fecha_fin")

    # Convertir las fechas a objetos `datetime`
    try:
        if fecha_inicio:
            fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        if fecha_fin:
            fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    except ValueError:
        return HttpResponse("Formato de fecha inválido. Use el formato AAAA-MM-DD.", status=400)

    # Filtrar registros por fecha si los parámetros están presentes
    asistencias = Asistencia.objects.all()
    if fecha_inicio:
        asistencias = asistencias.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        asistencias = asistencias.filter(fecha__lte=fecha_fin)

    # Configurar la respuesta HTTP para devolver un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_asistencia.pdf"'

    # Crear el objeto canvas de ReportLab
    pdf = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Título del reporte
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, height - 50, "Reporte de Asistencia")

    # Mostrar rango de fechas si está presente
    pdf.setFont("Helvetica", 12)
    if fecha_inicio or fecha_fin:
        rango = f"Del {fecha_inicio.strftime('%d/%m/%Y') if fecha_inicio else 'inicio'} al {fecha_fin.strftime('%d/%m/%Y') if fecha_fin else 'fin'}"
        pdf.drawString(50, height - 80, rango)

    # Columnas del reporte
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 100, "Profesor")
    pdf.drawString(200, height - 100, "Clase")
    pdf.drawString(350, height - 100, "Fecha")
    pdf.drawString(450, height - 100, "Asistencia")

    # Datos del modelo Asistencia
    y = height - 120  # Posición inicial de las filas
    pdf.setFont("Helvetica", 10)
    for asistencia in asistencias:
        # Escribir datos de cada registro en el PDF
        pdf.drawString(50, y, asistencia.profesor.nombre)
        pdf.drawString(200, y, asistencia.clase.nombre)
        pdf.drawString(350, y, asistencia.fecha.strftime("%d/%m/%Y"))
        pdf.drawString(450, y, "Asistió" if asistencia.asistencia else "No asistió")
        y -= 20  # Mover hacia abajo para la siguiente fila

        # Salto de página si se llena la página actual
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, height - 100, "Profesor")
            pdf.drawString(200, height - 100, "Clase")
            pdf.drawString(350, height - 100, "Fecha")
            pdf.drawString(450, height - 100, "Asistencia")
            y = height - 120

    # Finalizar el documento
    pdf.save()
    return response

# Create your views here.
def estudianteRead(request):
    # Recuperar parámetros de búsqueda y filtros desde la solicitud GET
    query = request.GET.get('q', '').strip()  # Parámetro de búsqueda por nombre
    semestre = request.GET.get('semestre')  # Parámetro para filtrar por semestre
    clase_id = request.GET.get('clase')  # Parámetro para filtrar por clase (materia)

    # Obtener todos los registros de estudiantes inicialmente
    estudiantes = Estudiante.objects.all()

    # Filtrar estudiantes por nombre si se proporciona un valor en 'q'
    if query:
        estudiantes = estudiantes.filter(nombre__icontains=query)  # Búsqueda parcial insensible a mayúsculas

    # Filtrar estudiantes por semestre si se proporciona un valor
    if semestre:
        estudiantes = estudiantes.filter(semestre=semestre)

    # Filtrar estudiantes por clase (materia) si se proporciona un valor
    if clase_id:
        estudiantes = estudiantes.filter(clase_id=clase_id)

    # Obtener todas las clases para mostrarlas como opciones de filtro en la plantilla
    clases = Clase.objects.all()

    # Crear un rango de semestres del 1 al 10 para usar como opciones de filtro en la plantilla
    semestres = range(1, 11)

    # Preparar los datos para enviarlos al contexto de la plantilla
    data = {
        'estudiantes': estudiantes,  # Lista de estudiantes filtrados
        'clases': clases,  # Lista de todas las clases disponibles
        'query': query,  # Parámetro de búsqueda para mostrar en el formulario
        'semestre': semestre,  # Semestre seleccionado para el filtro
        'clase_id': clase_id,  # ID de la clase seleccionada para el filtro
        'semestres': semestres,  # Rango de semestres (1 al 10) para el filtro
    }

    # Renderizar la plantilla 'estudianteRead.html' con los datos del contexto
    return render(request, 'estudianteRead.html', data)

#Insercion de datos
def estudianteCreate(request): 
    # Verifica si la solicitud es de tipo POST (cuando el usuario envía el formulario)
    if request.method == 'POST':
        # Crea una instancia del formulario `EstudianteForm` con los datos enviados
        form = EstudianteForm(request.POST)
        
        # Verifica si el formulario es válido (cumple con todas las validaciones del modelo)
        if form.is_valid():
            # Guarda los datos del formulario como un nuevo registro en la base de datos
            form.save()
            # Redirige al usuario a la vista 'estudianteRead', que probablemente lista todos los estudiantes
            return redirect('estudianteRead')
    
    else:  # Si la solicitud es de tipo GET (cuando el usuario carga la página inicialmente)
        # Crea una instancia vacía de `EstudianteForm` para mostrar un formulario vacío en la página
        form = EstudianteForm()

    # Renderiza la plantilla 'estudianteCreate.html', enviando el formulario en el contexto
    return render(request, 'estudianteCreate.html', {'form': form})

#Update
# Vista para actualizar los datos de un estudiante
def estudianteUpdate(request, id):
    # Obtiene la instancia del estudiante a partir del id proporcionado
    estudiante = Estudiante.objects.get(id=id)
    
    # Si la solicitud es de tipo GET (se quiere cargar el formulario con los datos actuales)
    if request.method == 'GET':
        # Se crea un formulario con la instancia del estudiante (cargando los datos actuales)
        form = EstudianteForm(instance=estudiante)
    else:
        # Si la solicitud es POST (se han enviado datos para actualizar el estudiante)
        # Se crea el formulario con los datos recibidos en request.POST y la instancia del estudiante
        form = EstudianteForm(request.POST, instance=estudiante)
        
        # Si el formulario es válido (los datos cumplen con las validaciones)
        if form.is_valid():
            # Guarda los cambios realizados en la base de datos
            form.save()
            # Redirige a la vista que muestra todos los estudiantes
            return redirect('estudianteRead')
    
    # Si no es un envío de formulario o hay errores, renderiza el formulario
    return render(request, 'estudianteCreate.html', {'form': form})

# Vista para eliminar un estudiante
def estudianteDelete(request, id):
    # Obtiene la instancia del estudiante a partir del id proporcionado
    estudiante = Estudiante.objects.get(id=id)
    
    # Si la solicitud es de tipo POST (el usuario ha confirmado la eliminación)
    if request.method == 'POST':
        # Elimina la instancia del estudiante de la base de datos
        estudiante.delete()
        # Redirige a la vista que muestra todos los estudiantes
        return redirect('estudianteRead')
    
    # Si la solicitud no es POST, muestra una página de confirmación para eliminar al estudiante
    return render(request, 'estudianteDelete.html', {'estudiante': estudiante})



# Vista para leer y filtrar los profesores
def profesorRead(request):
    # Recuperar los parámetros de búsqueda y filtros desde la solicitud GET
    query = request.GET.get('q', '').strip()  # Filtro por nombre o clave del profesor
    aula_id = request.GET.get('aula')  # Filtro por el ID de aula (aula en la que enseña el profesor)
    clase_id = request.GET.get('clase')  # Filtro por el ID de la clase (materia que enseña el profesor)

    # Obtener todos los profesores inicialmente (sin filtros)
    profesores = Profesor.objects.all()

    # Filtrar por nombre o clave si se proporciona un valor en 'q'
    if query:
        # Filtra los profesores cuyos nombres o claves contienen el valor 'query' (sin importar mayúsculas/minúsculas)
        profesores = profesores.filter(nombre__icontains=query) | profesores.filter(clave__icontains=query)
    
    # Filtrar por aula si se proporciona un 'aula_id'
    if aula_id:
        # Filtra los profesores que están asignados al aula con el ID correspondiente
        profesores = profesores.filter(aula_id=aula_id)
    
    # Filtrar por clase si se proporciona un 'clase_id'
    if clase_id:
        # Filtra los profesores que enseñan la clase (materia) con el ID correspondiente
        profesores = profesores.filter(clase_id=clase_id)

    # Obtener todos los objetos de Aula para usar en el filtro del template
    aulas = Aula.objects.all()

    # Obtener todos los objetos de Clase (materias) para usar en el filtro del template
    clases = Clase.objects.all()

    # Crear un diccionario con los datos a pasar al contexto del template
    data = {
        'profesores': profesores,  # La lista de profesores filtrados
        'aulas': aulas,  # La lista de aulas para el filtro en el template
        'clases': clases,  # La lista de clases (materias) para el filtro en el template
        'query': query,  # El término de búsqueda (si hay uno)
        'aula_id': aula_id,  # El ID del aula filtrado (si existe)
        'clase_id': clase_id,  # El ID de la clase filtrado (si existe)
    }
    
    # Renderiza la plantilla 'profesorRead.html' pasando los datos al contexto
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

# Vista para listar las asistencias de los estudiantes
def asistencia_lista(request):
    # Obtener todos los estudiantes, profesores, clases y aulas inicialmente
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    clases = Clase.objects.all()
    aulas = Aula.objects.all()

    # Recuperar los parámetros de filtro desde la solicitud GET
    nombre_profesor = request.GET.get('nombre_profesor', '')  # Filtro por nombre del profesor
    aula_id = request.GET.get('aula', '')  # Filtro por ID del aula
    clase_id = request.GET.get('clase', '')  # Filtro por ID de la clase (materia)

    # Si se proporciona un nombre de profesor, se filtran los profesores por ese nombre
    if nombre_profesor:
        profesores = profesores.filter(nombre__icontains=nombre_profesor)

    # Si se proporciona un aula, se filtran los profesores que están asignados a esa aula
    if aula_id:
        profesores = profesores.filter(aula_id=aula_id)

    # Si se proporciona una clase (materia), se filtran las asistencias de esa clase
    if clase_id:
        asistencias = Asistencia.objects.filter(clase_id=clase_id)
    else:
        # Si no se proporciona una clase, se obtienen todas las asistencias
        asistencias = Asistencia.objects.all()

    # Pasar los datos al template 'asistencia_lista.html' para su renderización
    return render(request, 'asistencia_lista.html', {
        'asistencias': asistencias,  # Las asistencias filtradas
        'estudiantes': estudiantes,  # Todos los estudiantes
        'profesores': profesores,    # Los profesores filtrados
        'clases': clases,            # Las clases (materias)
        'aulas': aulas,              # Las aulas
        'nombre_profesor': nombre_profesor,  # El nombre del profesor utilizado como filtro
        'aula_id': aula_id,                  # El ID del aula utilizado como filtro
        'clase_id': clase_id,                # El ID de la clase utilizado como filtro
    })
