from django.conf                                  import settings
from rest_framework                               import generics, status
from rest_framework.response                      import Response
from rest_framework.permissions                   import IsAuthenticated
from rest_framework_simplejwt.backends            import TokenBackend

from authAppComInd.models.producto                import Producto
from authAppComInd.models.cuenta                  import Cuenta
from authAppComInd.serializers.productoSerializer import ProductoSerializer

#se usa para ver un producto
class ProductoDetailView(generics.RetrieveAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)

#se usa para ver todos los productos creados por usuario
class ProductoCuentaView(generics.ListAPIView):
   serializer_class   = ProductoSerializer
   permission_classes = (IsAuthenticated,)

   def get_queryset(self):
       
       token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
       tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
       valid_data   = tokenBackend.decode(token,verify=False)
        
       if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
       queryset = Producto.objects.all()
       return queryset
    
#para crear productos
class ProductoCreateView(generics.CreateAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = ProductoSerializer(data=request.data['producto_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cuenta = Cuenta.objects.get(id=request.data['producto_data']['cuenta'])
        cuenta.cantidadProductos += request.data['producto_data']['cantidad']
        cuenta.save()

        return Response("Creacion de producto exitosa", status=status.HTTP_201_CREATED)

#para actualizar producto
class ProductoUpdateView(generics.UpdateAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Producto.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)

#para borrar producto
class ProductoDeleteView(generics.DestroyAPIView):
    serializer_class   = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    queryset           = Producto.objects.all()

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        super().destroy(request, *args, **kwargs)
        return Response("producto eliminado", status=status.HTTP_204_NO_CONTENT)
        