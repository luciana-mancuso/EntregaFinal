from django.db import models

# Create your models here.

class Destino(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=100, default="sin subtitulo")
    descripcion = models.TextField()
    autor = models.CharField(max_length=100, default='Autor: Luciana Mancuso')
    fecha= models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='destinos/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.comentario

    
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