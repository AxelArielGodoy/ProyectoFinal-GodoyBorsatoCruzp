from django.shortcuts import redirect, render, HttpResponse
from .models import Post
from LibreriaApp.forms import BusquedaPost, FormularioPost
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio.html')


def blog(request):
    return HttpResponse('blog')


def contacto(request):
    return HttpResponse("contacto")


def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")

@login_required
def crear_post(request):
    
    if request.method == "POST":
        
        formulario_post = FormularioPost(request.POST, request.FILES)
    
        if formulario_post.is_valid():
            
            informacion = formulario_post.cleaned_data
            
            post = Post(
                titulo = informacion['titulo'],
                subtitulo = informacion['subtitulo'],
                contenido = informacion['contenido'],
                autor = informacion['autor'],
                fecha_creacion = informacion['fecha_creacion'],
                imagen = informacion['imagen'],
            )
            post.save()
            
            return redirect('crear_post')
        
    else:
        formulario_post = FormularioPost()
    return render(request, 'crear_post.html', {'form': formulario_post})


@login_required
def buscar_post(request):

    titulo_de_busqueda = request.GET.get("titulo")

    if titulo_de_busqueda:
        listado_post = Post.objects.filter(titulo__icontains=titulo_de_busqueda)
    else:
        listado_post = Post.objects.all()

    form = BusquedaPost()
    return render(request, "buscar_post.html", {"listado_post": listado_post, "form": form})

@login_required
def editar_post(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormularioPost(request.POST, request.FILES)
        if form.is_valid():
            post.titulo = form.cleaned_data.get('titulo')
            post.subtitulo = form.cleaned_data.get('subtitulo')
            post.contenido = form.cleaned_data.get('contenido')
            post.autor = form.cleaned_data.get('autor')
            post.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            post.imagen = form.cleaned_data.get('imagen')
            post.save()
            
            return redirect('buscar_post')
        else:
            return render(request, "crear_post", {"form": formulario_post, "post": post})
    
    formulario_post = FormularioPost(initial={'titulo': post.titulo, 'subtitulo': post.subtitulo, 'contenido': post.contenido, 'autor': post.autor, 'fecha_creacion': post.fecha_creacion, 'imagen': post.imagen})
    
    return render(request, "editar_post.html", {"form": formulario_post, "post": post})


@login_required
def eliminar_post(request, id):
    
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('buscar_post')
@login_required
def ver_mas(request, id):
    post = Post.objects.get(id=id)
    return render(request, "ver_mas.html", {"post": post})