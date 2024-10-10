from django.db import models

class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', verbose_name='картинки')
    category = models.CharField(max_length=150, verbose_name='Категория')
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = 'Имя продукта'
        verbose_name_plural = 'Имена продуктов'
        ordering = ['name_product']