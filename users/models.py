from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField(null=True, blank=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    # to authenticate users
    USERNAME_FIELD = 'email'

    # for create superuser
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    # can user permissions to read models
    def has_module_perms(self, app_label):
        if self.is_admin:
            return True

    # users can be staff
    def is_staff(self):

        return self.is_admin