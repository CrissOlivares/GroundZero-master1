from django.urls import path
from . import views
from django.contrib import admin
urlpatterns=[
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
    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
]
