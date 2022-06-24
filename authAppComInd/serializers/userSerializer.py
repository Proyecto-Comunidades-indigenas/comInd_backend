from rest_framework                             import serializers
from authAppComInd.models.user                  import User
from authAppComInd.models.cuenta                import Cuenta
from authAppComInd.serializers.cuentaSerializer import CuentaSerializer

class UserSerializer(serializers.ModelSerializer):
    cuenta = CuentaSerializer()
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'nombreComunidad', 'oficio', 'region','cuenta']
    
    #con la data que me llega del json voy a crear un objeto usuario
    def create(self, validated_data):
        cuentaData  = validated_data.pop('cuenta')
        userInstance = User.objects.create(**validated_data)
        Cuenta.objects.create(user=userInstance, **cuentaData)
        return userInstance

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        cuenta  = Cuenta.objects.get(user=obj.id)
        return {
            'id'              : user.id,
            'email'           : user.email,
            'nombreComunidad' : user.nombreComunidad,
            'oficio'          : user.oficio,
            'region'          : user.region,
            'cuenta' : {
                'id'               : cuenta.id,
                'cantidadProductos': cuenta.cantidadProductos,
                'fecha'            : cuenta.fecha,
                'condicion'        : cuenta.condicion
            }
        }