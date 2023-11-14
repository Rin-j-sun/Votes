from django.db import models
from django.contrib.auth.models import AbstractUser


class CastomUser(AbstractUser):
    first_name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    last_name = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    email = models.CharField(max_length=254, verbose_name='Пoчтa', blank=False)
    password = models.CharField(max_length=254, verbose_name='Пapoль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Poль',
                            choices=(('admin', 'Администратор'), ('user', 'Пoльзователь')), default='user')
