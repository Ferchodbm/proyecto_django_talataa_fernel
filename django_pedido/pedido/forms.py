from django.forms import ModelForm
from .models import Pedido

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre',
                  'apellido',
                  'correo',
                  'telefono',
                  'direccion',
                  'fecha_entrega',
                  'franja_hora']