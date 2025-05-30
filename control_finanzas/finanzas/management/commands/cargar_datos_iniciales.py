from django.core.management.base import BaseCommand
from finanzas.models import Categoria

class Command(BaseCommand):
    help = 'Carga categorías de ejemplo para ingresos y gastos'

    def handle(self, *args, **options):
        # Categorías de Ingresos
        categorias_ingresos = [
            {'nombre': 'Salario', 'descripcion': 'Ingresos por trabajo'},
            {'nombre': 'Freelance', 'descripcion': 'Trabajos independientes'},
            {'nombre': 'Inversiones', 'descripcion': 'Rendimientos de inversiones'},
            {'nombre': 'Regalos', 'descripcion': 'Dinero recibido como regalo'},
            {'nombre': 'Ventas', 'descripcion': 'Ingresos por ventas'},
            {'nombre': 'Otros Ingresos', 'descripcion': 'Otros tipos de ingresos'},
        ]

        # Categorías de Gastos
        categorias_gastos = [
            {'nombre': 'Alimentación', 'descripcion': 'Comida y bebidas'},
            {'nombre': 'Transporte', 'descripcion': 'Gastos de movilidad'},
            {'nombre': 'Vivienda', 'descripcion': 'Alquiler, servicios, mantenimiento'},
            {'nombre': 'Salud', 'descripcion': 'Medicinas, consultas médicas'},
            {'nombre': 'Educación', 'descripcion': 'Cursos, libros, materiales'},
            {'nombre': 'Entretenimiento', 'descripcion': 'Ocio y diversión'},
            {'nombre': 'Ropa', 'descripcion': 'Vestimenta y accesorios'},
            {'nombre': 'Tecnología', 'descripcion': 'Dispositivos y software'},
            {'nombre': 'Servicios', 'descripcion': 'Internet, teléfono, etc.'},
            {'nombre': 'Otros Gastos', 'descripcion': 'Otros tipos de gastos'},
        ]

        # Crear categorías de ingresos
        for cat_data in categorias_ingresos:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                tipo='ingreso',
                defaults={'descripcion': cat_data['descripcion']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Categoría de ingreso creada: {categoria.nombre}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Categoría de ingreso ya existe: {categoria.nombre}')
                )

        # Crear categorías de gastos
        for cat_data in categorias_gastos:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                tipo='gasto',
                defaults={'descripcion': cat_data['descripcion']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Categoría de gasto creada: {categoria.nombre}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Categoría de gasto ya existe: {categoria.nombre}')
                )

        self.stdout.write(
            self.style.SUCCESS('¡Datos iniciales cargados exitosamente!')
        ) 