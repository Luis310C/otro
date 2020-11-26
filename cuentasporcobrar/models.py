from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Proveedor(models.Model):
    id_proveedor=models.BigAutoField(primary_key=True,null=False,blank=False)
    proveedor=models.CharField(max_length=50)
    total_deuda=models.FloatField()
    nombre_de_la_Empresa=models.CharField(max_length=50,null=True)
    nombre_del_contacto=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.proveedor



class Rol(models.Model):
    id_rol=models.BigAutoField(primary_key=True,null=False,blank=False)
    rol=models.CharField(max_length=50)   
    descripcion=models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion


class OpcionesMenu(models.Model):
    id_opcion=models.BigAutoField(primary_key=True,null=False,blank=False)
    opcion=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    id_rol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    def __str__(self):
        return self.opcion

class Estilo(models.Model):
    id_estilo=models.BigAutoField(primary_key=True,null=False,blank=False)
    estilo=models.CharField(max_length=50)
    ruta=models.FileField(upload_to='css/')
    def __str__(self):
        return self.estilo
    

class Usuario(models.Model):
    usuario=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    rol=models.ForeignKey(Rol,on_delete=models.CASCADE,default=Rol.objects.filter(id_rol=2).values('id_rol'))
    estilo=models.ForeignKey(Estilo,on_delete=models.CASCADE,default=Estilo.objects.filter(id_estilo=1).values('id_estilo'))
    
    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
              
             Usuario.objects.create(usuario=instance)
             
        instance.usuario.save()
      
    def __str__(self):
        return self.usuario.username
        

class articulo(models.Model):
    nombre=models.CharField(max_length=50)
    precio_venta=models.FloatField()
    costo_compra=models.FloatField()
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class pedido(models.Model):
    numero_pedido=models.BigAutoField(primary_key=True,null=False,blank=False)
    creacion=models.DateTimeField(auto_now_add=True)
    descripcion=models.TextField()
    Proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    total_adeudado=models.FloatField()
  


class cliente(models.Model):
    nombre=models.CharField(max_length=41)
    creacion=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()
    def __str__(self):
        return self.nombre

class venta(models.Model):
    numero_venta=models.BigAutoField(primary_key=True,null=False,blank=False)
    cliente=models.ForeignKey(cliente,on_delete=models.CASCADE)
    articulo=models.ForeignKey(articulo,on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    def _get_total(self):
        return self.cantidad*self.articulo.precio_venta
    total=property(_get_total)




class ordenpago(models.Model):
    numero_orden=models.BigAutoField(primary_key=True,null=False,blank=False)
    creacion=models.DateTimeField(auto_now_add=True)
    cantidad=models.FloatField()
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)


