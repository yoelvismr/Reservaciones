from django.urls import path

from apps.reservaciones.views import *

urlpatterns = [
    # Inicio
    path('', Index.as_view(), name='index'),
    # reservaciones
    path('reservacion/gastronomica/', ReservacionGastronmicaView.as_view(), name='reservaciones_gastronomicas'),
    path('reservacion/gastronomica/<int:pk>/', ReservacionGastronmicaCreateView.as_view(),
         name='crear_reservacion_gastronomica'),
    # path('reservacion/galeria/<int:pk>', ReservacionGaleriaView.as_view(), name='reservacion_galeria'),
]