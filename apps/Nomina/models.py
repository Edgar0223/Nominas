from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django import forms
from django.core.validators import MinValueValidator

# Create your models here.

class Nominas(models.Model):
    fechaInicio = models.DateField(auto_now_add=True)
    fechaFin = models.DateField(auto_now_add=True)
    pagoNomina = models.DecimalField(max_digits=10, decimal_places=3, validators=[MinValueValidator(0)])
    status = models.BooleanField(default=False)
    diasPagadas = models.IntegerField()
    empelado = models.ForeignKey('Empleados.Empleados', on_delete=models.CASCADE, related_name='empleados_en_departamento', null=True)
    def __str__(self):
        return f'{self.fechaInicio} {self.fechaFin} {self.pagoNomina}'


