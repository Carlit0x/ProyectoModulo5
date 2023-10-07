from django.shortcuts import render
from django.http import HttpResponse
from .models import Activo, Grupo


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse("Bienvenido " + name + " al Proyecto")

def grupos(request):
    post_grupo = request.POST.get("grupo")
    if post_grupo:
        q = Grupo(grupos=post_grupo)
        q.save()

    filtro_grupo = request.GET.get("grupo")
    if filtro_grupo:
        grupos = Grupo.objects.filter(
            nombre__regex=f"{filtro_grupo}$")
    else:
        grupos = Grupo.objects.all()
   
    return render(request, "grupos.html", {
        "titulo": "LISTA DE GRUPOS CONTABLES",
        "grupos": grupos
    })

def activos(request):
    post_activo = request.POST.get("activo")
    if post_activo:
        q = Activo(nombre=post_activo)
        q.save()

    filtro_activo = request.GET.get("activo")
    if filtro_activo:
        activos = Activo.objects.filter(
            nombre__regex=f"{filtro_activo}$")
    else:
        activos = Activo.objects.all()
    return render(request, "activos.html", {
        "titulo": "LISTA DE BIENES",
        "activos": activos
    })