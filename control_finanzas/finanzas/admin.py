from django.contrib import admin
from .models import Categoria, Transaccion

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'descripcion')
    list_filter = ('tipo',)
    search_fields = ('nombre',)

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'monto', 'categoria', 'usuario', 'fecha', 'descripcion')
    list_filter = ('tipo', 'categoria', 'fecha')
    search_fields = ('descripcion', 'categoria__nombre')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
