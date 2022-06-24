from django.db import models
from .cuenta  import Cuenta

class Producto(models.Model):
    id              = models.AutoField(primary_key=True)
    cuenta          = models.ForeignKey(Cuenta, related_name='producto_cuenta', on_delete=models.CASCADE)
    nombreProducto  = models.CharField(max_length=70)
    caracteristicas = models.CharField(max_length=200)
    fecha_registro  = models.DateTimeField(auto_now_add=True, blank=True)
    cantidad        = models.IntegerField(default=0)
    tipo_producto   = models.CharField(max_length=50)