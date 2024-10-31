from django.db import models
from django.utils import timezone



class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок блога')
    slug = models.SlugField(max_length=100, verbose_name="slug", help_text="slug")
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Уже тут')
    views_counter = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title} '

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
