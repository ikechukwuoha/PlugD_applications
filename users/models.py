from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyManager





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add = True, null=True)
    last_seen = models.DateTimeField(auto_now_add=True, null=True)


    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_pd_staff = models.BooleanField(default=False)


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    objects = MyManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_full_name(self):
        self.username

    def get_short_name(self):
        return self.first_name

    # def __str__(self):
    #     self.email