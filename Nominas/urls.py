from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('apps.Usuarios.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.Usuarios.urls')),
    path('departamentos/', include('apps.Departamentos.urls')),
    path('nomina/', include('apps.Nomina.urls')),
    path('materiaPrima/', include('apps.MateriaPrima.urls')),
    path('empleados/', include('apps.Empleados.urls')),
]
