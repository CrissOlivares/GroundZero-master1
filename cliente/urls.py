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
    path('login/', views.login_view, name='login'),
    # Otras URLs de tu aplicación
]
