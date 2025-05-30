from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Transaccion, Categoria
from .forms import IngresoForm, GastoForm, TransaccionForm

@login_required
def dashboard(request):
    # Calcular totales
    ingresos_total = Transaccion.objects.filter(
        usuario=request.user, 
        tipo='ingreso'
    ).aggregate(Sum('monto'))['monto__sum'] or 0
    
    gastos_total = Transaccion.objects.filter(
        usuario=request.user, 
        tipo='gasto'
    ).aggregate(Sum('monto'))['monto__sum'] or 0
    
    saldo = ingresos_total - gastos_total
    
    # Últimas transacciones
    ultimas_transacciones = Transaccion.objects.filter(
        usuario=request.user
    ).order_by('-fecha')[:10]
    
    # Totales por categoría este mes
    mes_actual = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    gastos_por_categoria = Transaccion.objects.filter(
        usuario=request.user,
        tipo='gasto',
        fecha__gte=mes_actual
    ).values('categoria__nombre').annotate(
        total=Sum('monto')
    ).order_by('-total')
    
    ingresos_por_categoria = Transaccion.objects.filter(
        usuario=request.user,
        tipo='ingreso',
        fecha__gte=mes_actual
    ).values('categoria__nombre').annotate(
        total=Sum('monto')
    ).order_by('-total')
    
    context = {
        'ingresos_total': ingresos_total,
        'gastos_total': gastos_total,
        'saldo': saldo,
        'ultimas_transacciones': ultimas_transacciones,
        'gastos_por_categoria': gastos_por_categoria,
        'ingresos_por_categoria': ingresos_por_categoria,
    }
    
    return render(request, 'finanzas/dashboard.html', context)

@login_required
def registrar_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.usuario = request.user
            transaccion.save()
            messages.success(request, '¡Ingreso registrado exitosamente!')
            return redirect('dashboard')
    else:
        form = IngresoForm()
    
    return render(request, 'finanzas/registrar_ingreso.html', {'form': form})

@login_required
def registrar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.usuario = request.user
            transaccion.save()
            messages.success(request, '¡Gasto registrado exitosamente!')
            return redirect('dashboard')
    else:
        form = GastoForm()
    
    return render(request, 'finanzas/registrar_gasto.html', {'form': form})

@login_required
def lista_transacciones(request):
    transacciones = Transaccion.objects.filter(usuario=request.user).order_by('-fecha')
    
    # Filtros
    tipo_filtro = request.GET.get('tipo')
    categoria_filtro = request.GET.get('categoria')
    
    if tipo_filtro:
        transacciones = transacciones.filter(tipo=tipo_filtro)
    
    if categoria_filtro:
        transacciones = transacciones.filter(categoria_id=categoria_filtro)
    
    categorias = Categoria.objects.all()
    
    context = {
        'transacciones': transacciones,
        'categorias': categorias,
        'tipo_filtro': tipo_filtro,
        'categoria_filtro': categoria_filtro,
    }
    
    return render(request, 'finanzas/lista_transacciones.html', context)

@login_required
def editar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = TransaccionForm(request.POST, instance=transaccion)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Transacción actualizada exitosamente!')
            return redirect('lista_transacciones')
    else:
        form = TransaccionForm(instance=transaccion)
    
    return render(request, 'finanzas/editar_transaccion.html', {
        'form': form, 
        'transaccion': transaccion
    })

@login_required
def eliminar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        transaccion.delete()
        messages.success(request, '¡Transacción eliminada exitosamente!')
        return redirect('lista_transacciones')
    
    return render(request, 'finanzas/eliminar_transaccion.html', {
        'transaccion': transaccion
    })

@login_required
def reportes(request):
    # Totales generales
    ingresos_total = Transaccion.objects.filter(
        usuario=request.user, 
        tipo='ingreso'
    ).aggregate(Sum('monto'))['monto__sum'] or 0
    
    gastos_total = Transaccion.objects.filter(
        usuario=request.user, 
        tipo='gasto'
    ).aggregate(Sum('monto'))['monto__sum'] or 0
    
    # Totales por categoría
    gastos_por_categoria = Transaccion.objects.filter(
        usuario=request.user,
        tipo='gasto'
    ).values('categoria__nombre').annotate(
        total=Sum('monto')
    ).order_by('-total')
    
    ingresos_por_categoria = Transaccion.objects.filter(
        usuario=request.user,
        tipo='ingreso'
    ).values('categoria__nombre').annotate(
        total=Sum('monto')
    ).order_by('-total')
    
    context = {
        'ingresos_total': ingresos_total,
        'gastos_total': gastos_total,
        'saldo': ingresos_total - gastos_total,
        'gastos_por_categoria': gastos_por_categoria,
        'ingresos_por_categoria': ingresos_por_categoria,
    }
    
    return render(request, 'finanzas/reportes.html', context)
