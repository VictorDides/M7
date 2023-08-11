from django.db import models
from sitio_web.models import Usuario


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    


class Pedido(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('en_preparacion', 'En preparación'),
        ('en_despacho', 'En despacho'),
        ('entregado', 'Entregado'),
    )
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vendedor = models.CharField(max_length=255)
    direccion_entrega = models.CharField(max_length=255)
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField()
    costo = models.IntegerField()
    forma_pago = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')



