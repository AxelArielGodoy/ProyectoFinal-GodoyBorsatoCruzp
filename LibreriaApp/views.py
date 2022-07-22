from django.shortcuts import redirect, render, HttpResponse
from .models import Post
from LibreriaApp.forms import BusquedaPost, FormularioPost

def inicio(request):
    return render(request, 'inicio.html')

# def crear_libro(request):
    
#     if request.method == "POST":
        
#         formulario_libro = FormularioLibro(request.POST)
    
#         if formulario_libro.is_valid():
            
#             informacion = formulario_libro.cleaned_data
            
#             libro = Libro(
#                 titulo = informacion['titulo'],
#                 autor = informacion['autor'],
#                 fecha_lanzamiento = informacion['fecha_lanzamiento'],
#                 idioma = informacion['idioma'],
#                 descripcion = informacion['descripcion'],
#                 precio = informacion['precio'],
#             )
#             libro.save()
            
#             return redirect('crear_libro')
        
#     else:
#         formulario_libro = FormularioLibro()
#     return render(request, 'crear_libro.html', {'form': formulario_libro})


def blog(request):
    return HttpResponse('blog')


def contacto(request):
    return HttpResponse("contacto")


def acerca_de(request):
    return HttpResponse("Acerca de")




def crear_post(request):
    
    if request.method == "POST":
        
        formulario_post = FormularioPost(request.POST)
    
        if formulario_post.is_valid():
            
            informacion = formulario_post.cleaned_data
            
            post = Post(
                titulo = informacion['titulo'],
                subtitulo = informacion['subtitulo'],
                contenido = informacion['contenido'],
                autor = informacion['autor'],
                fecha_creacion = informacion['fecha_creacion'],
                # imagen = informacion['imagen'],
            )
            post.save()
            
            return redirect('crear_post')
        
    else:
        formulario_post = FormularioPost()
    return render(request, 'crear_post.html', {'form': formulario_post})



def buscar_post(request):

    titulo_de_busqueda = request.GET.get("titulo")

    if titulo_de_busqueda:
        listado_post = Post.objects.filter(titulo__icontains=titulo_de_busqueda)
    else:
        listado_post = Post.objects.all()

    form = BusquedaPost()
    return render(request, "buscar_post.html", {"listado_post": listado_post, "form": form})

