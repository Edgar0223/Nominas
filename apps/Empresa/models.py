from django.db import models

# Create your models here.


class datosEmpresa(models.Model):
    nombre = models.CharField(max_length=254)
    razonSocial = models.CharField(max_length=254)
    rfc = models.CharField(max_length=254)
    direecion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    correo = models.CharField(max_length=254)
    vision = models.CharField(max_length=254)
    valores = models.CharField(max_length=254)
    mision = models.CharField(max_length=254)
    logo  = models.ImageField(upload_to='logo/', null=True, blank=True)
