from itertools import product
from tkinter import CASCADE
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

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('color', 'Cor'),
    ('size', 'Tamanho'),

)

    
class Variation(models.Model):
    product= models.ForeignKey(Product, on_delete= models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value