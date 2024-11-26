from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField




class User(AbstractUser):

    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='images/',
                               blank=True,
                               null=True,
                               verbose_name='картинки',
                               help_text='Можно добавить фото')

    number = PhoneNumberField(verbose_name='Номер телефона',
                                     null=True,
                                     blank=True,
                                     help_text='Введите свой номер')

    country = CountryField(max_length=150, verbose_name='Страна')

    token = models.CharField(max_length=150, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.email




