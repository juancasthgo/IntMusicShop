from django.contrib.auth.models import User
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from .forms import *
from django.db.models import Q
from django.views.generic.list import ListView
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404


from carritos.models import Carrito
from .models import Categoria, Producto

def inicio(request):
    productos13 = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'primeros_productos': productos13,
        'categorias': categorias,
    }
    return render(request, "inicio.html", context)

def home(request):
    productos13 = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'primeros_productos': productos13,
        'categorias': categorias,
    }
    return render(request, "home.html", context)

def acerca(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
    }
    return render(request, "acerca.html", context)

@permission_required('app.view_producto')
def resultado(request, categoria_id):
    categoria_id = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'id_cat': categoria_id,
    }
    return render(request, "search/resultado.html", context)


def producto(request, producto_id):
    categorias = Categoria.objects.all()
    un_producto =get_object_or_404(Producto, id=producto_id)
    carrito_obj, nuevo_carrito = Carrito.objects.new_or_get(request)
    context = {
        'producto': un_producto,
        'categorias': categorias,
        'carrito': carrito_obj,
    }
    return render(request, "product/producto.html", context)

@permission_required('app.view_producto')
def crear_producto(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = FormProducto(request.POST, request.FILES, 
            initial={'fecha':timezone.now()}, 
            instance=Producto(imagen=request.FILES['imagen'], 
            admin=user,            
            ))
        if form.is_valid():
            form.save()
            messages.success(request, "Producto Agregado")
            return redirect("productos:home")
    else:
        form = FormProducto(initial={'fecha':timezone.now()})
        categorias = Categoria.objects.all()
        return render(request, "product/producto_nuevo.html", {
            'categorias': categorias,
            "form": form
        })
    
@permission_required('app.view_producto')
def editar_producto(request, producto_id):
    producto_editado = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        producto_editado.admin = user
        form = FormProducto(data=request.POST, files=request.FILES, instance=producto_editado)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto Editado")
            return redirect("productos:home")
    else:
        form = FormProducto(instance = producto_editado)
        categorias = Categoria.objects.all()
        context = {
            'categorias': categorias,
            "producto": producto_editado,
            "form": form
        }
        return render(request, 'product/producto_editado.html', context)

@permission_required('app.view_producto')
def producto_borrado(request, producto_id):
    borrado = get_object_or_404(Producto, id=producto_id)
    borrado.delete()
    messages.success(request, "Producto Eliminado")
    return redirect("productos:home")

@permission_required('app.view_producto')
def categorias(request, categoria_id):
    categoria_id = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'id_cat': categoria_id,
    }
    return render(request, "base/navbar.html", context)

class SearchResultsView(ListView):
    model = Producto
    template_name = 'search/resultado.html'
        
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Producto.objects.filter(
             Q(titulo__icontains=query) | 
             Q(descripcion__icontains=query)
        )
        return object_list 
 
def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje Enviado")

        else:
            data["form"] = formulario

    return render(request, 'templates/inicio.html', data)

@permission_required('app.view_producto')
def categoria(request):
    data = {
        'form': CategoriaForm()
    }
    
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Marca Agregada")
        else:
            data["form"] = formulario

    return render(request, 'templates/categoria.html', data)


@permission_required('app.view_producto')
def listar(request):
    productos = Contacto.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(productos, 3)
        productos = paginator.page(page)
    except:
        raise Http404

    data = { 
        'entity': productos,
        'paginator': paginator
    }

    return render(request, "product/listar.html", data)
