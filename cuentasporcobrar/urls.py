"""cuentasporcobrar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/',usuarioNuevo.as_view(),name='registrar'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',inicio,name='home'),
    path('accounts/profile/',pantallainicio),
    path('menu/',menu.as_view(),name='menu'),
    path('editar/estilo',cambiarestilo.as_view(),name='cambiarestilo'),
    path('editar/perfil',editarperfil.as_view(),name='editarperfil'),
    path('agregar/rol',agregarRol.as_view(),name='agregarol'),
    path('agregar/estilo',agregarEstilo.as_view(),name='agregarestilo'),
    path('agregar/opcion',agregarOpcionMenu.as_view(),name='agregaropciomenu'),
    path('lista/opcion',ListarOpciones.as_view(),name='listaopcion'),
    path('editar/opcion/<int:pk>',editarOpcion.as_view(),name='editaropcion'),
    path('registratr/pago',crearOrdenPago.as_view(),name='pago'),
    path('registrar/cliente',registrarCliente.as_view(),name='nuevo-cliente'),
    path('registrar/producto',registrarProducto.as_view(),name='nuevo-producto'),
    path('registra/proveedor',registrarproveedor.as_view(),name='registrar-proveedor'),
    path('tabla/proveedor',tableproveedores.as_view(),name='proveedoresT'),
    path('tabla/usuarios',tableusuarios.as_view(),name='usuariosT'),
    path('tabla/cliente',tablecliente.as_view(),name='clienteT'),
    path('tabla/articulo',tablearticulo.as_view(),name='articuloT'),
    path('registrar/deuda',registrarDeuda.as_view(),name='registrar-deuda'),
    path('tabla/mod',tablamodificada.as_view(),name='tabla'),
    path('delete/<int:pk>',Deleteopcion.as_view(),name='deleteopcion' ),
    path('tabla/opcionesmenu',tablaopcionesMenu.as_view(),name='opcioneMenu'),
    path('truco/',editUser.as_view(),name='truco'),
    path('lista/rol',rollista.as_view(),name='listarol'),
    path('delete/rol/<int:pk>',DeleteRol.as_view(),name='deleterol'),
    path('edit/rol/<int:pk>',editRol.as_view(),name='editrol')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
