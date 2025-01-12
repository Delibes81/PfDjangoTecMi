from django.urls import path
from . import views

urlpatterns = [
    path('captura_datos_usuario/', views.captura_datos_usuario, name='captura_datos_usuario'),
    path('captura_datos_videos/<str:id_usuario>/<int:cantidad_videos>/', views.captura_datos_videos, name='captura_datos_videos'),
    path('resumen_videos/<str:id_usuario>/', views.resumen_videos, name='resumen_videos'),
]