
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    titulo       = models.CharField(max_length=260, null=False)
    imagen       = models.ImageField(upload_to='imagenes/')
    descripcion  = models.TextField()
    precio       = models.DecimalField(decimal_places=0, max_digits=20)
    categoria    = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha        = models.DateField(null= False)
    urlpago      = models.URLField(null=True)
    admin        = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=25)    
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
