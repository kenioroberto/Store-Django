# Generated by Django 4.1 on 2022-08-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('carts', '0003_alter_cart_options_alter_cartitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation', verbose_name='Variação'),
        ),
    ]
