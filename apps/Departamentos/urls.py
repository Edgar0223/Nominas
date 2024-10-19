from django.urls import path
from . import views

urlpatterns = [
    path('Departamentos/',views.index)
]

