from django.urls import path
from .views import *

urlpatterns = [
	path('gustos/',vista_gustos),
	path('lista_producto/',vista_lista_producto, name='vista_lista_producto'),
	path('agregar_producto/',vista_agregar_producto, name='vista_agregar_producto'),
]
