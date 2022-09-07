from django.db import models
from store.models import Product, Variation
from accounts.models import Account

class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True, verbose_name='ID')
    date_added = models.DateField(auto_now_add=True, verbose_name='Data de cadastro')

    def __str__(self):
        return self.cart_id

    class Meta:
        verbose_name = 'Carrinho'
        verbose_name_plural = 'Carrinhos'

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Produtos')
    variations = models.ManyToManyField(Variation, blank=True, verbose_name='Variação')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Carrinho', null=True)
    quantity = models.IntegerField(verbose_name='Quantidade')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
    
    class Meta:
        verbose_name = 'Carrinho Item'
        verbose_name_plural = 'Carrinhos Itens'

