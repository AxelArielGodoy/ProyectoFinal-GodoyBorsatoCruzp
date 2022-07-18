from django.shortcuts import render, HttpResponse

def inicio(request):
    return render(request, 'inicio.html')


def tienda(request):
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