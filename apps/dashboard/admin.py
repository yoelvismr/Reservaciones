from django.contrib import admin

from apps.reservaciones.models import ReservacionGastronmica, ReservacionAlojaminto, ReservacionTransporte

# Register your models here.
admin.site.register(ReservacionGastronmica)

admin.site.register(ReservacionAlojaminto)

admin.site.register(ReservacionTransporte)