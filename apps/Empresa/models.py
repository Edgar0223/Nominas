from django.db import models
from django.core.validators import EmailValidator

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

class Personas(models.Model):
    Nombre = models.CharField(max_length=254)
    rfc = models.CharField(max_length=254)
    razonSocial = models.CharField(max_length=254)
    direccion = models.CharField(max_length=254)
    pagina = models.CharField(max_length=254)
    telefono = models.CharField(max_length=13)
    caracterPersona = models.CharField(max_length=254)
    materiaP = models.ForeignKey('MateriaPrima.materiaPrima', on_delete=models.CASCADE, related_name='clientes_o_provedores_en_contacto', null=True)


class Contacto(models.Model):
    nombre = models.CharField(max_length=254)
    telefono = models.CharField(max_length=13)
    correo = models.EmailField(max_length=100, unique=True, validators=[EmailValidator(message="Introduce un correo válido.")])
    tipo = models.CharField(max_length=254)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='clientes_o_provedores_en_contacto', null=True)

