
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Pedido, Conductor
from .forms import PedidoForm
from .models import Pedido
import json
import random

# Create your views here.



def home(request):
    return render(request, 'home.html')

def pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido.html', {'pedidos': pedidos})


def detallePedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'GET':
        form = PedidoForm(instance=pedido)
        return render(request, 'detallePedido.html', {'pedido': pedido, 'form': form})
    else:
        form = PedidoForm(request.POST, instance=pedido)
        form.save()
        return redirect('pedido')


def eliminarPedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido')


def createPedido(request):
    if request.method == 'GET':
        return render(request, 'createPedido.html', {
            'form': PedidoForm
        })
    elif request.method == 'POST':
        try:
            form = PedidoForm(request.POST)
            nuevo_pedido = form.save(commit=False)
            c = random.choice(Conductor.objects.values().filter(estado=1))
            nuevo_pedido.conductor = c['id']
            if nuevo_pedido.franja_hora > 0 and nuevo_pedido.franja_hora < 9:
                nuevo_pedido.save()
                
                return redirect('pedido')
            else:
                return render(request, 'createPedido.html', {
                    'form': PedidoForm,
                    'error': 'No se puede crear mayor de 8h'
                })
        except:
            return render(request, 'createPedido.html', {
                'form': PedidoForm,
                'error': 'Datos errados, favor volver a digitar'
            })


def conductor(request):
    conductores = Conductor.objects.all()
    return render(request, 'conductor.html', {'conductores': conductores})


def detalleConductor(request, conductor_id):
    conductor = get_object_or_404(Conductor, pk=conductor_id)
    pedidos = Pedido.objects.filter(conductor=conductor_id)
    return render(request, 'detalleConductor.html', {'conductor': conductor, 'pedidos': pedidos})
