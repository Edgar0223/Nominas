from django.db import models
from django.core.validators import EmailValidator


class Empleados(models.Model):
    nombres = models.CharField(max_length=50, null=False)
    apellidos = models.CharField(max_length=50, null=False)
    procedencia = models.CharField(max_length=25, null=False)
    fechaInicio = models.DateField()
    telefono = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100, unique=True, validators=[EmailValidator(message="Introduce un correo válido.")])
    foto  = models.ImageField(upload_to='fotosEmpleados/', null=True, blank=True)
    rol = models.CharField(max_length=254, null=False)
    Salario = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tipoNomina = models.CharField(max_length=254, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    class Meta:
        ordering = ['nombres']
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

class DocumentosEmpleado(models.Model):
    contrato  = models.ImageField(upload_to='documentosEmpleados/contratos', null=True, blank=True)
    actaNacimiento  = models.ImageField(upload_to='documentosEmpleados/actaNacimiento', null=True, blank=True)
    identificacion  = models.ImageField(upload_to='documentosEmpleados/identificacion', null=True, blank=True)
    comDomicilio  = models.ImageField(upload_to='documentosEmpleados/comDomicilio', null=True, blank=True)
    seguroSocial  = models.ImageField(upload_to='documentosEmpleados/SeguroSocial', null=True, blank=True)
    empleado = models.OneToOneField(Empleados, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Documentos de {self.empleado.nombres} {self.empleado.apellidos}'
    
    class Meta:
        verbose_name = 'Documento de Empleado'
        verbose_name_plural = 'Documentos de Empleados'