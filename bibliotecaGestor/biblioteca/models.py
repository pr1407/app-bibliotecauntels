from django.db import models

# Create your models here.
from datetime import datetime


class Libro(models.Model):
    idLibro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anioPublicacion = models.DateTimeField()
    stock = models.IntegerField()
    status = models.BooleanField(default=True)

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Prestamo(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPrestamo = models.DateTimeField(default=datetime.now)
    fechaDevolucion = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)