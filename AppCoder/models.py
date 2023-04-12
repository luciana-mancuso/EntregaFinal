from django.db import models

# Create your models here.

class Destino(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='destinos/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    
class Alojamiento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Museo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo