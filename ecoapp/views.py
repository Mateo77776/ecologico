from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Reciclaje, Plantacion
from .forms import ReciclajeForm, PlantacionForm

def es_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# --- DASHBOARD ADMINISTRATIVO ---
@login_required
def dashboard(request):
    total_reciclajes = Reciclaje.objects.count()
    kilos_totales = Reciclaje.objects.aggregate(Sum('peso_kg'))['peso_kg__sum'] or 0
    total_plantaciones = Plantacion.objects.count()
    arboles_totales = Plantacion.objects.aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    total_usuarios = User.objects.count()

    context = {
        'total_reciclajes': total_reciclajes,
        'kilos_totales': kilos_totales,
        'total_plantaciones': total_plantaciones,
        'arboles_totales': arboles_totales,
        'total_usuarios': total_usuarios,
        'es_admin': es_admin(request.user),
    }
    return render(request, 'ecoapp/dashboard.html', context)

# ================= CRUD RECICLAJE =================
@login_required
def lista_reciclaje(request):
    registros = Reciclaje.objects.all().order_by('-fecha_registro')
    return render(request, 'ecoapp/lista_reciclaje.html', {
        'registros': registros,
        'es_admin': es_admin(request.user)
    })

@login_required
def crear_reciclaje(request):
    if request.method == 'POST':
        form = ReciclajeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.success(request, '¡Registro de reciclaje guardado correctamente!')
            return redirect('lista_reciclaje')
        else:
            messages.error(request, 'Error al guardar el registro. Verifica que los datos sean válidos.')
    else:
        form = ReciclajeForm()
    return render(request, 'ecoapp/formulario.html', {'form': form, 'titulo': 'Registrar Reciclaje', 'volver': 'lista_reciclaje'})

@user_passes_test(es_admin, login_url='lista_reciclaje')
def editar_reciclaje(request, pk):
    obj = get_object_or_404(Reciclaje, pk=pk)
    if request.method == 'POST':
        form = ReciclajeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro de reciclaje actualizado correctamente!')
            return redirect('lista_reciclaje')
        else:
            messages.error(request, 'Error al actualizar el registro. Revisa los campos ingresados.')
    else:
        form = ReciclajeForm(instance=obj)
    return render(request, 'ecoapp/formulario.html', {'form': form, 'titulo': 'Editar Reciclaje', 'volver': 'lista_reciclaje'})

@user_passes_test(es_admin, login_url='lista_reciclaje')
def eliminar_reciclaje(request, pk):
    obj = get_object_or_404(Reciclaje, pk=pk)
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, 'Registro de reciclaje eliminado correctamente.')
        except Exception:
            messages.error(request, 'Ocurrió un error al intentar eliminar el registro de reciclaje.')
        return redirect('lista_reciclaje')
    return render(request, 'ecoapp/confirmar_eliminar.html', {'objeto': obj, 'volver': 'lista_reciclaje'})

# ================= CRUD PLANTACIÓN =================
@login_required
def lista_plantacion(request):
    registros = Plantacion.objects.all().order_by('-fecha_plantacion')
    return render(request, 'ecoapp/lista_plantacion.html', {
        'registros': registros,
        'es_admin': es_admin(request.user)
    })

@login_required
def crear_plantacion(request):
    if request.method == 'POST':
        form = PlantacionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            messages.success(request, '¡Plantación registrada exitosamente!')
            return redirect('lista_plantacion')
        else:
            messages.error(request, 'Error al registrar la plantación. Verifica que los datos sean válidos.')
    else:
        form = PlantacionForm()
    return render(request, 'ecoapp/formulario.html', {'form': form, 'titulo': 'Registrar Plantación', 'volver': 'lista_plantacion'})

@user_passes_test(es_admin, login_url='lista_plantacion')
def editar_plantacion(request, pk):
    obj = get_object_or_404(Plantacion, pk=pk)
    if request.method == 'POST':
        form = PlantacionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Plantación actualizada correctamente!')
            return redirect('lista_plantacion')
        else:
            messages.error(request, 'Error al actualizar la plantación. Revisa los campos ingresados.')
    else:
        form = PlantacionForm(instance=obj)
    return render(request, 'ecoapp/formulario.html', {'form': form, 'titulo': 'Editar Plantación', 'volver': 'lista_plantacion'})

@user_passes_test(es_admin, login_url='lista_plantacion')
def eliminar_plantacion(request, pk):
    obj = get_object_or_404(Plantacion, pk=pk)
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, 'Plantación eliminada correctamente.')
        except Exception:
            messages.error(request, 'Ocurrió un error al intentar eliminar la plantación.')
        return redirect('lista_plantacion')
    return render(request, 'ecoapp/confirmar_eliminar.html', {'objeto': obj, 'volver': 'lista_plantacion'})