from django.shortcuts import render, redirect, get_object_or_404
from .models import Canal
from django.urls import reverse
from django.http import HttpResponse

# -------------------------------
# CRUD para MODELO: VIDEO
# -------------------------------
from .models import Video, Canal

def agregar_video(request):
    canales = Canal.objects.all()
    if request.method == 'POST':
        canal_id = request.POST.get('canal')
        canal = Canal.objects.get(id=canal_id)
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        duracion_horas = int(request.POST.get('duracion_horas') or 0)
        duracion_min = int(request.POST.get('duracion_min') or 0)
        duracion_seg = int(request.POST.get('duracion_seg') or 0)
        vistas = int(request.POST.get('vistas') or 0)
        publico = bool(request.POST.get('publico'))
        url_miniatura = request.POST.get('url_miniatura')
        likes = request.POST.get('likes')

        from datetime import timedelta
        duracion = timedelta(hours=duracion_horas, minutes=duracion_min, seconds=duracion_seg)

        Video.objects.create(
            canal=canal,
            titulo=titulo,
            descripcion=descripcion,
            duracion=duracion,
            vistas=vistas,
            publico=publico,
            url_miniatura=url_miniatura,
            likes=likes
        )
        return redirect('ver_video')
    return render(request, 'video/agregar_video.html', {'canales': canales})


def ver_video(request):
    videos = Video.objects.select_related('canal').all()
    return render(request, 'video/ver_video.html', {'videos': videos})


def actualizar_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    canales = Canal.objects.all()
    if request.method == 'POST':
        canal_id = request.POST.get('canal')
        video.canal = Canal.objects.get(id=canal_id)
        video.titulo = request.POST.get('titulo')
        video.descripcion = request.POST.get('descripcion')
        duracion_horas = int(request.POST.get('duracion_horas') or 0)
        duracion_min = int(request.POST.get('duracion_min') or 0)
        duracion_seg = int(request.POST.get('duracion_seg') or 0)
        from datetime import timedelta
        video.duracion = timedelta(hours=duracion_horas, minutes=duracion_min, seconds=duracion_seg)
        video.vistas = int(request.POST.get('vistas') or 0)
        video.publico = bool(request.POST.get('publico'))
        video.url_miniatura = request.POST.get('url_miniatura')
        video.likes = request.POST.get('likes')
        video.save()
        return redirect('ver_video')
    return render(request, 'video/actualizar_video.html', {'video': video, 'canales': canales})


def borrar_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('ver_video')
    return render(request, 'video/borrar_video.html', {'video': video})


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


