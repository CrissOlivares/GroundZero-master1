from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import genero, cliente

# Registro de modelos:
admin.site.register(genero)
admin.site.register(cliente)

