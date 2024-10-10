from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'
        ordering = ['name']