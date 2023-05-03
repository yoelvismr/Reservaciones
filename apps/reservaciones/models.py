from django.db import models

from apps.dashboard.models import Entidad


# Create your models here.
class ReservacionGastronmica(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre de Cliente')
    cantidad_persona = models.PositiveIntegerField(verbose_name='Cantidad de Personas')
    fecha = models.DateField(verbose_name='Fecha de Reservación')
    hora = models.TimeField(verbose_name='Hora de Reservación')


class ReservacionAlojaminto(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre de Cliente')
    ci = models.PositiveIntegerField(verbose_name='Carnet de Identidada')
    cantidad_persona = models.PositiveIntegerField(verbose_name='Cantidad de Personas')
    fecha = models.DateField(verbose_name='Fecha de Reservación')
    cantidad_dia = models.PositiveIntegerField(verbose_name='Cantidad de Días')


class ReservacionTransporte(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre de Cliente')
    cantidad_persona = models.PositiveIntegerField(verbose_name='Cantidad de Personas')
    lugar = models.CharField(max_length=100, verbose_name='Lugar de Recogida')
    fecha = models.DateField(verbose_name='Fecha de Reservación')
    hora = models.TimeField(verbose_name='Hora de Reservación')
