from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Register(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Persona (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class IntegrantesEmpresa (models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)