from rest_framework                            import status, views
from rest_framework.response                   import Response
from rest_framework_simplejwt.serializers      import TokenObtainPairSerializer
from authAppComInd.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):
    def post(self,request, *args, **kwargs):
         serializer = UserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()

         tokenData = {"email":request.data["email"],
                    "password":request.data["password"]}
         try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
         except Exception as e:
            print(e)
            return Response('Error in en la generación del token', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
