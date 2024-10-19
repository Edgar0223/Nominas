from django.urls import path
from . import views
urlpatterns = [
    path('',views.banner),
    path('banner/',views.banner)
]
