from django.urls import path
from . import views
from django.contrib import admin
from .views import lista_clientes, agregar_cliente, actualizar_cliente, eliminar_cliente
app_name = 'clientes'

urlpatterns=[
    path('', lista_clientes, name='lista_clientes'),
    path('agregar/', agregar_cliente, name='agregar_cliente'),
    path('actualizar/<int:pk>/', actualizar_cliente, name='actualizar_cliente'),
    path('eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),

    path('',views.GroundZeroInicio,name="GroundZeroInicio.html"),
    path('GorundZeroCompra.html',views.GorundZeroCompra,name="GorundZeroCompra.html"),
    path('GroundZeroArtistas.html',views.GroundZeroArtistas,name="GroundZeroArtistas.html"),
    path('GroundZeroCuadros.html',views.GroundZeroCuadros,name="GroundZeroCuadros.html"),
    path('GroundZeroEsculturas.html',views.GroundZeroEsculturas,name="GroundZeroEsculturas.html"),
    path('GroundZeroOrfebreria.html',views.GroundZeroOrfebreria,name="GroundZeroOrfebreria.html"),
    path('GroundZeroLogin.html',views.GroundZeroLogin,name="GroundZeroLogin.html"),
    path('GroundZeroRegister.html',views.GroundZeroRegister,name="GroundZeroRegister.html"),
    path('GroundZeroPaises.html',views.GroundZeroPaises,name="GroundZeroPaises.html"),
    path('GroundZeropPQ.html',views.GroundZeropPQ,name="GroundZeropPQ.html"),
    path('GroundZeroInicio.html',views.GroundZeroInicio,name="GroundZeroInicio.html"),
    path('index.html',views.index,name="index.html"),
  #crud 
]
