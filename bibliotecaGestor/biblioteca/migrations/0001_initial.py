# Generated by Django 3.2.7 on 2022-06-14 19:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('idLibro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('anioPublicacion', models.DateTimeField()),
                ('stock', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('idPrestamo', models.AutoField(primary_key=True, serialize=False)),
                ('fechaPrestamo', models.DateTimeField(default=datetime.datetime.now)),
                ('fechaDevolucion', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=True)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.cliente')),
                ('idLibro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
            ],
        ),
    ]
