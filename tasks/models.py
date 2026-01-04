
## tasks/models.py
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    foto = models.ImageField(upload_to='perfiles/', blank=True)

    def __str__(self):
        return self.usuario.username

class Experiencia(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    url = models.URLField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)