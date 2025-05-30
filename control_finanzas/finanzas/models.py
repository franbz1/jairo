from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_tipo_display()} - ${self.monto} - {self.categoria.nombre}"
    
    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ['-fecha']
