from django.contrib import admin

from .models.user import User
from .models.cuenta import Cuenta
from .models.producto import Producto

admin.site.register(User)
admin.site.register(Cuenta)
admin.site.register(Producto)