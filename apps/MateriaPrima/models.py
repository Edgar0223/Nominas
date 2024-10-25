from django.db import models

# Create your models here.
class Area(models.Model):
    nombre =  models.CharField(max_length=255)
    unbicacion = models.CharField(max_length=255)

class materiaPrima(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    incioZafra = models.DateField(auto_now_add=True)
    finZafra = models.DateField(auto_now_add=True)

class Procesos(models.Model):
    nombre = models.CharField(max_length=255)
    fecha =  models.DateField(auto_now_add=True)
    areas  = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='areas_en_procesos', null=True)
    materia  = models.ForeignKey(materiaPrima, on_delete=models.CASCADE, related_name='materia_utizada_en_procesos', null=True)
