from django.db                   import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
         if not email:
            raise ValueError('La comunidad debe tener un correo electronico')
         user = self.model(email=email)
         user.set_password(password)
         user.save(using=self._db)
         return  user
    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email   = email,
            password= password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
   
class User(AbstractBaseUser, PermissionsMixin):
    id              = models.BigAutoField(primary_key=True)
    username        = None
    email           = models.EmailField('Email', max_length = 100, unique=True)
    password        = models.CharField('Password', max_length = 256)
    nombreComunidad = models.CharField('Nombre', max_length = 50)
    oficio          = models.CharField('Oficio',   max_length = 20)
    region          = models.CharField('Region', max_length = 50)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects     = UserManager()
    USERNAME_FIELD = 'email'