from django.urls import path
from . import views

urlpatterns = [
    path('nomina/',views.index)
]
