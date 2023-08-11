from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm

def registro(request):
    if request.method == "POST":
        formulario_p = RegistroUsuarioForm(request.POST)
        if formulario_p.is_valid():
            formulario_p.save()
            return redirect('landing')
        else:
            messages.error("Error de Registro")
    formulario = RegistroUsuarioForm()
    return render(request,'sitio_web/registro.html',{'formulario': formulario})
