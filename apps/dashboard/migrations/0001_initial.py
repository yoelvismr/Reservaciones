# Generated by Django 4.2.1 on 2023-05-03 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, verbose_name='Nombre de Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre de Entidad')),
                ('imagen', models.ImageField(upload_to='entidad', verbose_name='Imagen de Portada')),
                ('descripcion', models.TextField(max_length=250, verbose_name='Descripción de la Entidad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.categoria', verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(unique='galeria', upload_to='', verbose_name='Imagen')),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.entidad', verbose_name='Entidad')),
            ],
        ),
    ]
