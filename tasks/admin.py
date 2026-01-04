# tasks/admin.py
from django.contrib import admin
from .models import Perfil, Experiencia, Habilidad, Proyecto

admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Habilidad)
admin.site.register(Proyecto)