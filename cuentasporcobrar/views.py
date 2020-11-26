from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import *
from  .models import *
from django.db import models
from django.urls import reverse_lazy
from django.db.models import F
from django_tables2 import SingleTableView
from .tabla import  tablausuario


class tablamodificada(SingleTableView):
    model=Usuario
    table_class=tablausuario
    template_name='usuarios-tabla.html'


def inicio(request):
    return render(request,'index.html')

class usuarioNuevo(CreateView):
     form_class=registroForm
     template_name='registration/register.html'
     success_url=reverse_lazy('login')

class menu(LoginRequiredMixin,ListView):
     model=OpcionesMenu
     template_name='menu.html'
     def get_queryset(self):
        return OpcionesMenu.objects.filter(id_rol__gte=self.request.user.usuario.rol.id_rol).order_by('opcion')

class cambiarestilo(LoginRequiredMixin,UpdateView):
    model=Usuario
    fields=['estilo']
    template_name='actualizar.html'
    success_url=reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Cambiar estilo'}
        return context
    def get_object(self):
        return self.request.user.usuario

def pantallainicio(request):
    return render(request,'registration/accounts_profile.html')

class editarperfil(LoginRequiredMixin,UpdateView):
    form_class=edit_profile
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')
    def get_object(self):
          return self.request.user
class agregarRol(LoginRequiredMixin,CreateView):
    model=Rol
    template_name='crear.html'
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Agregar rol'}
        return context
    success_url=reverse_lazy('home')

class agregarEstilo(LoginRequiredMixin,CreateView):
    model=Estilo
    template_name='crear.html'
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Agregar estilo'}
        return context
    success_url=reverse_lazy('home')

class agregarOpcionMenu(LoginRequiredMixin,CreateView):
    model=OpcionesMenu
    template_name='crear.html'
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Agregar Opcion Menu'}
        return context
    success_url=reverse_lazy('menu')

class ListarOpciones(LoginRequiredMixin,ListView):
    queryset=OpcionesMenu.objects.all()
    template_name='lista.html'

class editarOpcion(LoginRequiredMixin,UpdateView):
    model=OpcionesMenu
    template_name='actualizar.html'
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Modificar Opcion'}
        return context
    success_url=reverse_lazy('menu')



class crearOrdenPago(LoginRequiredMixin,CreateView):
    model=ordenpago
    fields='__all__'
    template_name='crear.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Generar Pago'}
        return context
    success_url=reverse_lazy('proveedoresT')
    def form_valid(self,form):
        cantidad=form.cleaned_data['cantidad']
        proveedor=form.cleaned_data['proveedor']
        Proveedor.objects.filter(proveedor=proveedor).update(total_deuda=F('total_deuda')-cantidad)
        return super().form_valid(form)


class registrarCliente(LoginRequiredMixin,CreateView):
    model=cliente
    fields='__all__'
    template_name='crear.html'
    success_url=reverse_lazy('clientesT')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Registrar Cliente'}
        return context

class registrarproveedor(LoginRequiredMixin,CreateView):
    model=Proveedor
    fields='__all__'
    template_name='crear.html'
    success_url=reverse_lazy('proveedoresT')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Registrar proveedor'}
        return context

class tableproveedores(ListView):
    model=Proveedor
    template_name='tabla.html'

class tableusuarios(ListView):
    model=Usuario
    template_name='tabla.html'

class tablecliente(ListView):
    model=cliente
    template_name='tabla.html'
    

class tablearticulo(ListView):
    model=articulo
    template_name='tabla.html'

class registrarProducto(LoginRequiredMixin,CreateView):
    model=articulo
    fields='__all__'
    template_name='crear.html'
    success_url=reverse_lazy('articuloT')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Registrar articulo'}
        return context

class registrarDeuda(LoginRequiredMixin,CreateView):
    model=pedido
    fields='__all__'
    template_name='crear.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = {'titulo':'Registrar aumento de deuda'}
        return context
    success_url=reverse_lazy('proveedoresT')
    def form_valid(self,form):
        cantidad=form.cleaned_data['total_adeudado']
        proveedor=form.cleaned_data['Proveedor']
        Proveedor.objects.filter(proveedor=proveedor).update(total_deuda=F('total_deuda')+cantidad)
        return super().form_valid(form)