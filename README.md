# Control de Finanzas

Sistema de control de finanzas personales desarrollado con Django y Bootstrap.

## Características

- 📊 Dashboard con resumen financiero
- 💰 Registro de ingresos y gastos
- 📈 Reportes y análisis financiero
- 🏷️ Categorización de transacciones
- 🔒 Sistema de autenticación
- 📱 Diseño responsive con Bootstrap

## Requisitos

- Python 3.8 o superior
- Django 5.2
- Bootstrap 5.3
- SQLite3 (base de datos por defecto)

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd control_finanzas
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Realizar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Cargar datos iniciales:
```bash
python manage.py cargar_datos_iniciales
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## Uso

1. Acceder a `http://localhost:8000/admin` para gestionar usuarios y categorías
2. Iniciar sesión en `http://localhost:8000` con las credenciales creadas
3. Comenzar a registrar ingresos y gastos

## Estructura del Proyecto

```
control_finanzas/
├── control_finanzas/     # Configuración del proyecto
├── finanzas/            # Aplicación principal
│   ├── templates/       # Plantillas HTML
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas
│   └── forms.py         # Formularios
├── manage.py            # Script de gestión
└── requirements.txt     # Dependencias
```

## Funcionalidades Principales

- **Dashboard**: Vista general de ingresos, gastos y saldo
- **Registro de Transacciones**: Formularios para ingresos y gastos
- **Lista de Transacciones**: Historial completo con filtros
- **Reportes**: Análisis detallado de finanzas
- **Categorías**: Gestión de categorías de ingresos y gastos