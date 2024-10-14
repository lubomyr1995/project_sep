from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as v
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['-id']

    email = models.EmailField(unique=True, validators=(
        v.RegexValidator(*RegexEnum.EMAIL.value),
    ))
    password = models.CharField(_('password'), max_length=128, validators=(
        v.RegexValidator(*RegexEnum.PASSWORD.value),
    ))
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
