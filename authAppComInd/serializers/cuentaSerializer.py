from rest_framework                             import serializers
from authAppComInd.models.cuenta                import Cuenta
from authAppComInd.models.user                  import User

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['cantidadProductos','fecha','condicion']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.user_id)
        cuenta = Cuenta.objects.get(id=obj.id)
        return {
            'id'                : cuenta.id,
            'cantidadProductos' : cuenta.cantidadProductos,
            'fecha'             : cuenta.fecha,
            'condicion'         : cuenta.condicion,
            'user' : {
                'id'              : user.id,
                'nombreComunidad' : user.nombreComunidad,
            }
        }