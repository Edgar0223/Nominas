from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('apps.Usuarios.urls')),
    path('admin/', admin.site.urls),
    path('Usuarios/', include('apps.Usuarios.urls')),
    path('Departamentos/', include('apps.Departamentos.urls')),
    path('Nomina/', include('apps.Nomina.urls')),
    path('MateriaPrima/', include('apps.MateriaPrima.urls')),
    path('Empleados/', include('apps.Empleados.urls')),
]
