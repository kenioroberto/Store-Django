from pydoc import ModuleScanner
from django.db import models
from accounts.models import Account
from store.models import Product, Variation


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100) # este é o valor total pago
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, verbose_name='Cliente')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Pagamento')
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    phone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    address_line_1 = models.CharField(max_length=50, verbose_name='Endereço')
    address_line_2 = models.CharField(max_length=50, blank=True, verbose_name='Complemento')
    country = models.CharField(max_length=50, verbose_name='Bairro')
    state = models.CharField(max_length=50, verbose_name='Estado')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    order_note = models.CharField(max_length=100, blank=True, verbose_name='OBS: Venda')
    order_total = models.FloatField(verbose_name='Total pago')
    tax = models.FloatField(verbose_name='Taxas')
    status = models.CharField(max_length=10, choices=STATUS, default='New', verbose_name='Status')
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(serf):
        return f'{serf.first_name} {serf.last_name}'

    def full_address(serf):
        return f'{serf.address_line_1} {serf.address_line_2}'

    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name
