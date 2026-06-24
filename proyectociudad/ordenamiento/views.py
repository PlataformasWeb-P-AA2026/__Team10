from django.shortcuts import render, redirect
from ordenamiento.models import Parroquia, BarrioCiudadela
from ordenamiento.forms import ParroquiaForm, BarrioCiudadelaForm
# Create your views here.

def index(request):
    """ Muestra la página principal con los conteos básicos """
    lista_parroquias = Parroquia.objects.all()
    lista_barrios = BarrioCiudadela.objects.all()

    contexto = {
        'parroquias': lista_parroquias,
        'numero_parroquias': len(lista_parroquias),
        'barrios': lista_barrios,
        'numero_barrios': len(lista_barrios)
    }
    return render(request, 'index.html', contexto)


def listar_parroquias(request):
    """ Obtiene todas las parroquias usando el ORM """
    lista_parroquias = Parroquia.objects.all()
    
    contexto = {
        'parroquias': lista_parroquias,
        'numero_parroquias': len(lista_parroquias)
    }
    return render(request, 'listarParroquias.html', contexto)


def listar_barrios(request):
    """ Obtiene todos los barrios usando el ORM """
    lista_barrios = BarrioCiudadela.objects.all()
    
    contexto = {
        'barrios': lista_barrios,
        'numero_barrios': len(lista_barrios)
    }
    return render(request, 'listarBarrios.html', contexto)


def crear_parroquia(request):
    """ Procesa el formulario para guardar una nueva parroquia """
    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index) # Redirige al inicio tras guardar
    else:
        # Si no es POST, envía un formulario vacío
        formulario = ParroquiaForm()

    contexto = {'formulario': formulario}
    return render(request, 'crearParroquia.html', contexto)


def editar_parroquia(request, id):
    """ Busca una parroquia por ID y la edita """
    parroquia_editar = Parroquia.objects.get(pk=id)

    if request.method == 'POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia_editar)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia_editar)

    contexto = {'formulario': formulario}
    return render(request, 'editarParroquia.html', contexto)


def crear_barrio(request):
    """ Procesa el formulario para guardar un nuevo barrio """
    if request.method == 'POST':
        formulario = BarrioCiudadelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioCiudadelaForm()

    contexto = {'formulario': formulario}
    return render(request, 'crearBarrio.html', contexto)


def editar_barrio(request, id):
    """ Busca un barrio por ID y lo edita """
    barrio_editar = BarrioCiudadela.objects.get(pk=id)

    if request.method == 'POST':
        formulario = BarrioCiudadelaForm(request.POST, instance=barrio_editar)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioCiudadelaForm(instance=barrio_editar)

    contexto = {'formulario': formulario}
    return render(request, 'editarBarrio.html', contexto)


