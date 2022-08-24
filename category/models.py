from distutils.command.upload import upload
from django.urls import reverse
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True, verbose_name='Categoria Nome')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True, verbose_name='Descrição')
    cat_image = models.ImageField(upload_to = 'photos/categories', blank=True, verbose_name='Imagem')

    def __str__(self):
        return self.category_name

        

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
