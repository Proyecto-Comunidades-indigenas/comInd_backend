from django.db      import models
from .user     import User

class Cuenta(models.Model):
    id                  = models.AutoField(primary_key=True)
    user                = models.ForeignKey(User, related_name='cuenta', on_delete=models.CASCADE)
    cantidadProductos   = models.IntegerField(default=0)
    fecha               = models.DateTimeField()
    condicion           = models.BooleanField(default=True)