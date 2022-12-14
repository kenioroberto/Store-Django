# Generated by Django 4.1 on 2022-09-06 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line_1',
            field=models.CharField(max_length=50, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, max_length=100, verbose_name='OBS: Venda'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(verbose_name='Total pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment', verbose_name='Pagamento'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax',
            field=models.FloatField(verbose_name='Taxas'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
    ]
