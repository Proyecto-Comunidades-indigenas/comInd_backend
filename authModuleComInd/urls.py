from django.contrib                 import admin
from django.urls                    import path
from authAppComInd                  import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from drf_spectacular.views          import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/',                                admin.site.urls),
    path('login/',                                TokenObtainPairView.as_view()), # usa credenciales que retornan tokens)
    path('refresh/',                              TokenRefreshView.as_view()), # genera un nuevo access token
    path('user/',                                 views.UserCreateView.as_view()), # crea un nuevo usuario
    path('user/<int:pk>/',                        views.UserDetailView.as_view()), # muestra la informacion especifica de un usuario basado en el id(pk)
    path('cuenta/list/<int:user>/',               views.ListcuentaView.as_view()),
    path('cuenta/cuentaComunidades/<int:user>/',  views.ListOtrasCuentasView.as_view()),
    path('producto/<int:user>/<int:pk>/',         views.ProductoDetailView.as_view()),
    path('producto/create/',                      views.ProductoCreateView.as_view()),
    path('producto/productoLista/<int:user>/',    views.ProductoCuentaView.as_view()),
    path('producto/update/<int:user>/<int:pk>/',  views.ProductoUpdateView.as_view()),
    path('producto/delete/<int:user>/<int:pk>/',  views.ProductoDeleteView.as_view()),

    path('api/schema/',                           SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',                SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',                     SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]
