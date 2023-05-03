from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(unique=True, max_length=20, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombre


class Entidad(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre de Entidad')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    imagen = models.ImageField(upload_to='entidad', verbose_name='Imagen de Portada')
    descripcion = models.TextField(max_length=250, verbose_name='Descripción de la Entidad')

    def __str__(self):
        return self.nombre


class Galeria(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, verbose_name='Entidad')
    imagen = models.ImageField(unique='galeria', verbose_name='Imagen')
