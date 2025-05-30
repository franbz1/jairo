from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registrar-ingreso/', views.registrar_ingreso, name='registrar_ingreso'),
    path('registrar-gasto/', views.registrar_gasto, name='registrar_gasto'),
    path('transacciones/', views.lista_transacciones, name='lista_transacciones'),
    path('transacciones/editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('transacciones/eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),
    path('reportes/', views.reportes, name='reportes'),
] 