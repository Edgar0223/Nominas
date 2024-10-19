from django.urls import path
from . import views

urlpatterns = [
    path('materiaprima/',views.index)
]

