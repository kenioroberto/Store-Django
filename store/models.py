from django.urls import reverse
from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True, verbose_name='Nome Produto')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    description = models.TextField(max_length=500, blank=True, verbose_name='Descrição')
    price = models.IntegerField(verbose_name='Preço')
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField(verbose_name='Estoque')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    created_date = models.DateTimeField(auto_now_add=True)
    modifield_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    