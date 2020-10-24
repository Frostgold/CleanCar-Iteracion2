from django.db import models

# Create your models here.

class Instalacion(models.Model):
    cod       = models.IntegerField(primary_key=True)
    name      = models.CharField(max_length=30)
    direccion = models.TextField()
    imagen    = models.ImageField(upload_to='instalaciones', null=True)

    def __str__(self):
        return self.name
    

class Empleado(models.Model):
    cod         = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=30)
    imagen      = models.ImageField(upload_to='empleados', null=True)

    def __str__(self):
        return self.name

class Insumo(models.Model):
    name        = models.CharField(max_length=120, primary_key=True)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    descripcion = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
class Slider(models.Model):
    cod = models.IntegerField(primary_key=True)
    imagen = models.ImageField(upload_to='slider')

class Vision(models.Model):
    name        = models.CharField(max_length=20, primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.name
    
