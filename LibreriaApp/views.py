from django.shortcuts import redirect, render, HttpResponse
from .models import Libro
from LibreriaApp.forms import FormularioLibro

def inicio(request):
    return render(request, 'inicio.html')

def crear_libro(request):
    
    if request.method == "POST":
        
        formulario_libro = FormularioLibro(request.POST)
    
        if formulario_libro.is_valid():
            
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
            
            return redirect('crear_libro')
        
    else:
        formulario_libro = FormularioLibro()
    return render(request, 'crear_libro.html', {'form': formulario_libro})


def blog(request):
    return HttpResponse('blog')


def contacto(request):
    return HttpResponse("contacto")


def acerca_de(request):
    return HttpResponse("Acerca de")
