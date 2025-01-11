

from videos.models import TBL_Usuario, TBL_Video, TBL_VideoUsuario
import re

def pedir_datos_usuario():
    while True:
        id_usuario = input("Ingrese su Id (número de nómina): ")
        if not re.match("^[A-Za-z0-9]+$", id_usuario):
            print("Nómina en formato incorrecto. Debe capturar solo números y letras.")
            continue

        nombre_usuario = input("Ingrese su nombre: ")
        if not re.match("^[A-Za-z]+$", nombre_usuario):
            print("Nombre de usuario en formato incorrecto. Debe capturar solo letras.")
            continue

        try:
            cantidad_videos = int(input("Ingrese la cantidad de videos que subirá: "))
        except ValueError:
            print("Cantidad de videos en formato incorrecto. Debe capturar solo números.")
            continue

        return id_usuario, nombre_usuario, cantidad_videos

def pedir_datos_videos(cantidad_videos):
    videos = []
    formatos_validos = ['mpg', 'mov', 'mp4', 'avi', 'mkv']
    for i in range(cantidad_videos):
        while True:
            titulo_video = input(f"Ingrese el título del video {i+1}: ")
            if not re.match("^[A-Za-z0-9 ]+$", titulo_video):
                print("Título del video en formato incorrecto. Debe capturar solo números y letras.")
                continue

            extension_video = input(f"Ingrese la extensión del video {i+1} (mpg, mov, mp4, avi, mkv): ")
            if extension_video not in formatos_validos:
                print("Extensión de video no válida.")
                continue

            try:
                tamano_video = int(input(f"Ingrese el tamaño del video {i+1} en MB: "))
            except ValueError:
                print("Tamaño del video en formato incorrecto. Debe capturar solo números.")
                continue

            videos.append((titulo_video, extension_video, tamano_video))
            break
    return videos

def guardar_datos(id_usuario, nombre_usuario, videos):
    usuario = TBL_Usuario(nombre=nombre_usuario, id_nomina=id_usuario)
    usuario.save()


    for titulo_video, extension_video, tamano_video in videos:
        video = TBL_Video(nombre_video=titulo_video, extension_video=extension_video, tamano_video=tamano_video)
        video.save()
        video_usuario = TBL_VideoUsuario(id_usuario=usuario, id_video=video)
        video_usuario.save()

def main():
    id_usuario, nombre_usuario, cantidad_videos = pedir_datos_usuario()
    videos = pedir_datos_videos(cantidad_videos)
    guardar_datos(id_usuario, nombre_usuario, videos)
    print("Datos guardados exitosamente en la base de datos Pro_Gol.")

if __name__ == "__main__":
    main()

