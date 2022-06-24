from rest_framework                  import serializers
from authAppComInd.models.cuenta     import Cuenta
from authAppComInd.models.producto   import Producto
from authAppComInd.models.user       import User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombreProducto','caracteristicas','fecha_registro','cantidad','tipo_producto','cuenta']

    def to_representation(self, obj):
        cuenta    = Cuenta.objects.get(id=obj.cuenta_id)
        user      = User.objects.get(id=cuenta.user_id)
        producto  = Producto.objects.get(id=obj.id)
        return {
            'id'              : producto.id,
            'nombreProducto'  : producto.nombreProducto,
            'caracteristicas' : producto.caracteristicas,
            'fecha_registro'  : producto.fecha_registro,
            'cantidad'        : producto.cantidad,
            'tipo_producto'   : producto.tipo_producto,
            'cuenta' : {
                'id'        : cuenta.id,
                'condicion ': cuenta.condicion,
            },
            'user' : {
                'id'               : user.id,
                'nombreComunidad'  : user.nombreComunidad
            }
        }