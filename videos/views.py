from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TBL_Usuario, TBL_Video, TBL_VideoUsuario
import re

def home(request):
    return redirect('captura_datos_usuario')

def captura_datos_usuario(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        nombre_usuario = request.POST.get('nombre_usuario')
        cantidad_videos = int(request.POST.get('cantidad_videos'))

        # Validaciones
        if not re.match("^[A-Za-z0-9]+$", id_usuario):
            return HttpResponse('Nómina en formato incorrecto. Debe capturar solo números y letras.')
        if not re.match("^[A-Za-z ]+$", nombre_usuario):
            return HttpResponse('Nombre de usuario en formato incorrecto. Debe capturar solo letras.')

        # Guardar usuario
        usuario, created = TBL_Usuario.objects.get_or_create(id_nomina=id_usuario, defaults={'nombre': nombre_usuario})
        print(f"Usuario guardado: {usuario}, creado: {created}")

        return redirect('captura_datos_videos', id_usuario=id_usuario, cantidad_videos=cantidad_videos)

    return render(request, 'videos/captura_datos_usuario.html')

def captura_datos_videos(request, id_usuario, cantidad_videos):
    if request.method == 'POST':
        videos = []
        for i in range(cantidad_videos):
            nombre_video = request.POST.get(f'nombre_video_{i}')
            extension_video = request.POST.get(f'extension_video_{i}')
            tamano_video = request.POST.get(f'tamano_video_{i}')

            # Validaciones
            if not re.match("^[A-Za-z0-9 ]+$", nombre_video):
                return HttpResponse('Título del video en formato incorrecto. Debe capturar solo números y letras.')
            if extension_video not in ['mpg', 'mov', 'mp4', 'avi', 'mkv']:
                return HttpResponse('Extensión de video no válida.')
            if not tamano_video.isdigit() or int(tamano_video) > 3:
                return HttpResponse('Tamaño del video en formato incorrecto o mayor a 3 MB.')

            videos.append((nombre_video, extension_video, tamano_video))

        # Guardar videos y asociarlos al usuario
        try:
            usuario = TBL_Usuario.objects.get(id_nomina=id_usuario)
        except TBL_Usuario.DoesNotExist:
            return HttpResponse('Usuario no encontrado.')

        for nombre_video, extension_video, tamano_video in videos:
            video = TBL_Video(nombre_video=nombre_video, extension_video=extension_video, tamano_video=tamano_video)
            video.save()
            video_usuario = TBL_VideoUsuario(id_usuario=usuario, id_video=video)
            video_usuario.save()

        return redirect('resumen_videos', id_usuario=id_usuario)

    return render(request, 'videos/captura_datos_videos.html', {'cantidad_videos': range(cantidad_videos)})

def resumen_videos(request, id_usuario):
    usuario = TBL_Usuario.objects.get(id_nomina=id_usuario)
    videos_usuario = TBL_VideoUsuario.objects.filter(id_usuario=usuario)
    historial_videos = TBL_VideoUsuario.objects.all()

    return render(request, 'videos/resumen_videos.html', {
        'usuario': usuario,
        'videos_usuario': videos_usuario,
        'historial_videos': historial_videos
    })