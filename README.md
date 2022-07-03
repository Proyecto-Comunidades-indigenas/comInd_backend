# Proyecto de Ciclo III: Inventario productos comunidades indigenas - arquitectura monolítica
Este proyecto está enfocado en la creación de una aplicación web que permita de forma sistemática el almacenamiento y gestion de inventarios de productos elaborados por las comunidades indigenas del pais y en una versión siguiente de manera adicional se planea mejorar el frontend con imagenes referentes a cada producto ingresado.

### Backend: autenticación de usuarios
para la realizacion de este microservicio se utilizo el framework django, con el lenguaje de programacion python, las pruebas correspondientes se realizaron en postman 

### Contenido de Este repositorio: 

 1. Se tiene una carpeta llamada authAppComInd donde donde se administran las aplicaciones que el proyecto este utiliza, esta carpeta contiene las carpetas: models, migrations, serializers y views, asi como los archivos admin.py, apps.py y test.py. 

 2. Se tiene una carpeta llamada authModuleComInd donde se guardan todas las configuraciones del servidor del componente, esta carpeta contiene los archivos: asgi.py, settings_dev.py, settings_prod.py, urls.py y wsgi.py. 

 3. se creo un archivo procfile el cual es un archivo para declarar qué comandos ejecuta la aplicación en la plataforma Heroku

 4. se tienen dos archivos que permiten iniciar un servidor web de manera local y en la nube, estos archivos son manage_dev.py y manage.py

 ### Requerimientos 
```
 Django==3.2.8
 djangorestframework==3.12.4
 djangorestframework-simplejwt==4.8.0
 django-cors-headers
 PyJWT==2.1.0
 psycopg2-binary==2.9.1
 gunicorn
 django-heroku
```

### Ejecución del proyecto

para ejecutar el proyecto en local:

1. Se descarga el proyecto comprimido o se clona de GitHub
   ```
    git clone https://github.com/Proyecto-Comunidades-indigenas/comInd_backend.git
   ```
2. Al tener el proyecto en el ordenador, por la consola de comandos de ingresa al proyecto utilizando el comando cd:
   ```
    cd comInd_backend-main
   ```
3. se debe inicializar el entorno virtual:

   ```
    env/Scripts/activate
   ```
4. se debe ingresar el siguiente comando para ejecutar el proyecto en local(computador personal o servidor):

   ```
    python manage_dev.py runserver 
   ```
El proyecto se encuentra desplegado en la plataforma heroku:

https://com-ind-frontend.herokuapp.com/#/user/inicio

### Diagrama de despliegue 

la parte sombreada hace referencia al despliegue de componentes de la parte backend del proyecto

![image](https://user-images.githubusercontent.com/84297258/175609307-797dc175-4444-45ec-85a6-5427f8d98a48.png)


### Documentación de API

https://app.swaggerhub.com/apis/InventarioProdComInd/inventario-productos_comunidades_indigenas/1.0.0

### Pruebas

La ejecución de los casos de prueba se hizo por medio de la aplicacion postman:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/17863004-3e80648b-358b-4546-a590-602b23661d6f?action=collection%2Ffork&collection-url=entityId%3D17863004-3e80648b-358b-4546-a590-602b23661d6f%26entityType%3Dcollection%26workspaceId%3D7bcc2d18-e9d7-4ab3-8b52-f701bc8801d1)
