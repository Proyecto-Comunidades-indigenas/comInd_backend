from django.conf                                  import settings
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend

from authAppComInd.models.cuenta                import Cuenta
from authAppComInd.serializers.cuentaSerializer import CuentaSerializer


class ListcuentaView(generics.ListAPIView):
    serializer_class   = CuentaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Cuenta.objects.filter(user_id=self.kwargs['user'])
        return queryset


class ListOtrasCuentasView(generics.ListAPIView):
    serializer_class   = CuentaSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        queryset = Cuenta.objects.exclude(user_id=self.kwargs['user'])
        return queryset