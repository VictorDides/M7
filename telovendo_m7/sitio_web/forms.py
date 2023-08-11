from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Ingrese un correo valido')
    rut = forms.CharField(max_length=10, required=True, help_text='Ingrese su Rut sin punto ni guión')
    nombres = forms.CharField(max_length=50, required=True, help_text='Obligatorio.')
    apellidos = forms.CharField(max_length=50, required=True, help_text='Obligatorio.')
    
    class Meta:
        model = Usuario
        fields = ['rut', 'nombres', 'apellidos', 'email']

        
    
