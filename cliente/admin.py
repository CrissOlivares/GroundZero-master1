from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Genero, usuario

# Registro de modelos:
admin.site.register(Genero)
admin.site.register(usuario)

