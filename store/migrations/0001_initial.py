# Generated by Django 4.1 on 2022-08-21 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True, verbose_name='Nome Produto')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Descrição')),
                ('price', models.IntegerField(verbose_name='Preço')),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField(verbose_name='Estoque')),
                ('is_available', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modifield_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]