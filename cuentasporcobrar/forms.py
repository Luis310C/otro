from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django import forms

class registroForm(UserCreationForm):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label='Nombre',max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label='Apellido',max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))

   
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')    
    def __init__(self,*args,**kwargs):
        super(registroForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].label='Nombre de usuario'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].label='Contraseña'
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].label='Confirmar Contraseña'


class edit_profile(UserChangeForm):
   email=forms.EmailField(label='Correo Electronico',widget=forms.EmailInput(attrs={"class":"form-control"}))
   first_name=forms.CharField(label='Nombre',max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   username=forms.CharField(label='Usuario',max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   last_name=forms.CharField(label='Apellido',max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
   is_active=forms.CharField(label='activo',max_length=100,widget=forms.CheckboxInput(attrs={"class":"form-control"}))
   class Meta:
       model=User
       fields=('email','username','last_name','first_name','is_active','password')


    

    


