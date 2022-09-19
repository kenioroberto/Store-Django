from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Usuário deve conter um endereço de email')

        if not username:
            raise ValueError('Usuário deve conter um username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email= self.normalize_email(email),
            username= username,
            password= password,
            first_name= first_name,
            last_name= last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    username =  models.CharField(max_length=50, unique=True, verbose_name='Username')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=50, verbose_name='Telefone')

    #requered
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name= 'Data cadastro')
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='Ultimo Login')
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, verbose_name='Usuario')
    address_line_1 = models.CharField(blank=True, max_length=100, verbose_name='Endereço')
    address_line_2 = models.CharField(blank=True, max_length=100, verbose_name='Complemento')
    profile_picture = models.ImageField(upload_to = 'userprofile', blank=True, verbose_name='Imagem')
    city = models.CharField(blank=True, max_length=20, verbose_name='Cidade')
    country = models.CharField(blank=True, max_length=20, verbose_name='Bairro')
    state = models.CharField(blank=True, max_length=20, verbose_name='Estado')

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

