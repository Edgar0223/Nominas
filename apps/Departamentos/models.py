from django.db import models
from Empleados.models import Empleados

class Departamento(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    personasnecesarias = models.IntegerField(null=False)
    responsabilidades = models.TextField(null=False)
    responsable = models.OneToOneField(Empleados, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.nombre
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'