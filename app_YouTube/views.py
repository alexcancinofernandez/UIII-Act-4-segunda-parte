from django.shortcuts import render, redirect, get_object_or_404
from .models import Canal
from django.urls import reverse
from django.http import HttpResponse

def inicio_YouTube(request):
    # página principal del sistema
    return render(request, 'inicio.html', {'titulo': 'Sistema de Administración YouTube'})

def agregar_canal(request):
    if request.method == 'POST':
        # sin validación (según indicación)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_creacion = request.POST.get('fecha_creacion')  # YYYY-MM-DD
        suscriptores = request.POST.get('suscriptores') or 0
        url_personalizada = request.POST.get('url_personalizada')
        pais = request.POST.get('pais')
        categoria_principal = request.POST.get('categoria_principal')

        Canal.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            suscriptores=int(suscriptores),
            url_personalizada=url_personalizada,
            pais=pais,
            categoria_principal=categoria_principal
        )
        return redirect('ver_canal')
    return render(request, 'canal/agregar_canal.html')


def ver_canal(request):
    canales = Canal.objects.all().order_by('id')
    return render(request, 'canal/ver_canal.html', {'canales': canales})


def actualizar_canal(request, canal_id):
    canal = get_object_or_404(Canal, pk=canal_id)
    if request.method == 'POST':
        # aquí también podrías redirigir a una función separada, pero usaremos POST directo
        canal.nombre = request.POST.get('nombre')
        canal.descripcion = request.POST.get('descripcion')
        canal.fecha_creacion = request.POST.get('fecha_creacion')
        canal.suscriptores = int(request.POST.get('suscriptores') or 0)
        canal.url_personalizada = request.POST.get('url_personalizada')
        canal.pais = request.POST.get('pais')
        canal.categoria_principal = request.POST.get('categoria_principal')
        canal.save()
        return redirect('ver_canal')
    return render(request, 'canal/actualizar_canal.html', {'canal': canal})


def borrar_canal(request, canal_id):
    canal = get_object_or_404(Canal, pk=canal_id)
    if request.method == 'POST':
        canal.delete()
        return redirect('ver_canal')
    return render(request, 'canal/borrar_canal.html', {'canal': canal})