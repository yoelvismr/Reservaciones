from django.contrib import admin

from apps.dashboard.models import Categoria, Entidad, Galeria

# Register your models here.
admin.site.register(Categoria)

admin.site.register(Entidad)

admin.site.register(Galeria)
