from django.shortcuts import render, HttpResponse
from .models import Libro
from LibreriaApp.forms import FormularioLibro

def inicio(request):
    return render(request, 'inicio.html')

def crear_libro(request):
    
    if request.method == "POST":
        
        formulario_libro = FormularioLibro(request.POST)
    
        if formulario_libro.is_valid:
            
            informacion = formulario_libro.cleaned_data
            
            libro = Libro(
                titulo = informacion['titulo'],
                autor = informacion['autor'],
                fecha_lanzamiento = informacion['fecha_lanzamiento'],
                idioma = informacion['idioma'],
                descripcion = informacion['descripcion'],
                precio = informacion['precio'],
            )
            libro.save()
            
            return render(request, 'crear_libro.html')
        
    else:
        formulario_libro = FormularioLibro()
    return render(request, 'crear_libro.html', {'form': formulario_libro})


def tienda(request):
    titulo_de_busqueda = request.GET.get('titulo')
    if titulo_de_busqueda:
        listado_libros = Libro.objects.filter(titu)
    return render(request, 'tienda.html')


def blog(request):
    return HttpResponse("Blog")


def contacto(request):
    return HttpResponse("contacto")


def acerca_de(request):
    return HttpResponse("Acerca de")


def iniciar_sesion(request):
    return HttpResponse("Iniciar Sesión")


def registrarse(request):
    return HttpResponse("Registrarse")