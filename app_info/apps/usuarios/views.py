from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarUsuariosForm


# Create your views here.

class RegistrarUsuario (CreateView): 
    model= Usuario
    template_name= 'usuarios/registrar.html'
    form_class= RegistrarUsuariosForm
    success_url= reverse_lazy('inicio')