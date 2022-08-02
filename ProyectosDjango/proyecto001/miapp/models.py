from email.policy import default
from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    creado = models.DateField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now = True)
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion =models.CharField(max_length=250)
    creado = models.DateField()

class Carrera(models,Model):
    idcarrera = models.IntegerField()
    nombre = models.CharField(max_length=150)
    nombrecorto = models.CharField(max_length=20)
    imagen = models.ImageField()
    estado = models.CharField(max_length=1)