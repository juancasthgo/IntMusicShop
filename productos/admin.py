from django.contrib import admin

from productos.forms import CategoriaForm, ContactoForm
from .models import  Categoria, Contacto, Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Contacto)



# MODELO VISUALIZAR CONTACTO.
class ContactoProductoEdit(admin.ModelAdmin):
    list_display = ["nombre","correo","mensaje"]
    list_editable = ["mensaje"]
    search_fields = ["correo","nombre"]
    list_per_page =  10


# MODELO VISUALIZAR CONTACTO.
class CategoriaEdit(admin.ModelAdmin):
    list_display = ["nombre"]
    list_editable = ["nombre"]
    search_fields = ["nombre"]
    list_per_page =  10

