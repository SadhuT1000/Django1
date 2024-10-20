# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    names = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='картинки')
    category = models.CharField(max_length=150, verbose_name='Категория')
    group = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.names}'

    class Meta:
        verbose_name = 'Имя продукта'
        verbose_name_plural = 'Имена продуктов'
        ordering = ['names']
