# comentarios/views.py
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import *


def hello(request):
    return render(request, 'inicio.html')

def botones(request):
    return render(request, 'bienvenida.html')

def formu_dpto(request):
    form = DptoForm(request.POST)
    if form.is_valid():
            # Si el formulario es válido, guarda el nuevo departamento en la base de datos
            form.save()
            form = DptoForm()
     # Redirige a una página de éxito o lista

    else:
        messages.error(request, "Hubo un error al guardar los datos. Por favor, revisa los campos.")
        #form = DptoForm()  # Si es un GET, muestra un formulario vacío

    return render(request, 'form_dpto.html', {'form': form})

def formu_mpio(request):
    form = MpioForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_dpto.html', {'form': form})

def formu_suc(request):
    form = SucForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_sucursal.html', {'form': form})

def formu_cliente(request):
    form = ClienteForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_cliente.html', {'form': form})

def formu_prenda(request):
    form = PrendaForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_prenda.html', {'form': form})

def formu_armario(request):
    form = ArmarioForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_armario.html', {'form': form})

def formu_factura(request):
    form = FacturaForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_factura.html', {'form': form})


def formu_lavadora(request):
    form = LavadoraForm()  # Solo creamos el formulario sin validación ni procesamiento de datos
    return render(request, 'form_lavadora.html', {'form': form})


def comentario_view(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            lavado = form.cleaned_data['lavado']  # Obtenemos el valor seleccionado de los radio buttons
            
            # Procesamos los datos recibidos (en este caso los mostramos en la plantilla)
            return render(request, 'exito.html', {'comentario': comentario, 'lavado': lavado})
    else:
        form = ComentarioForm()

    return render(request, 'index2.html', {'form': form})


def departamentos_list(request):
    # Consultar todos los registros de la tabla Departamento
    departamentos = departamento.objects.all()

    # Pasar los registros a la plantilla
    return render(request, 'departamentos_list.html', {'departamentos': departamentos})
