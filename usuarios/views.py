

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from productos.models import Categoria
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreation

def registro(request):
    data = { 
        'form': CustomUserCreation()
    }

    if request.method == 'POST':
        formulario = CustomUserCreation(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registracion Exitosa, Bienvenido")
            return render(request, "home.html")

        data["form"] = formulario 
    return render(request, 'registration/register.html', data)

