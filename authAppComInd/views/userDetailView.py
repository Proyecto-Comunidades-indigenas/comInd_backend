from django.conf                              import settings
from rest_framework                           import generics, status
from rest_framework.response                  import Response
from rest_framework.permissions               import IsAuthenticated
from rest_framework_simplejwt.backends        import TokenBackend

from authAppComInd.models.user                import User
from authAppComInd.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
     queryset           = User.objects.all()
     serializer_class   = UserSerializer
     permission_classes = (IsAuthenticated,)#tupla con solo un elemento por eso lleva ,

     def get(self, request, *args, **kwargs):
        #se hace un request solicitando el token que esta en authorization a partir del caracter 7
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        #validacion del token que se solicito en la petición, se genera el token con el algoritmo de settings 
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        #decodificacion del token que recibi, y verificación si el token se genero con el algoritmo de settings
        valid_data   = tokenBackend.decode(token,verify=False)
        
        #verificación que el usuario que solicita el token 
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Acceso no autorizado'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)

