import django_tables2 as tables
from .models import *

class tablausuario(tables.Table):
    email=tables.Column(accessor="usuario.email")
    contraseña=tables.Column(accessor="usuario.password")
    nombre=tables.Column(accessor="usuario.username")
    class Meta:
        model=Usuario
        fields=('rol','estilo')
        sequence=('nombre','email','contraseña','rol','estilo')


