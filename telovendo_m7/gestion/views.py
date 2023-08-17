from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Pedido  

@method_decorator(login_required, name='dispatch')
class ListaPedidosView(ListView):
    model = Pedido
    template_name = 'lista_pedidos.html'
    context_object_name = 'pedidos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tomar_pedido_url'] = reverse_lazy('tomar_pedido')
        return context
