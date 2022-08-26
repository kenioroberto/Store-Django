# Generated by Django 4.1 on 2022-08-24 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category', verbose_name='Categoria'),
        ),
    ]
