from django.conf import settings
from django.db import models
from django.utils import timezone
from product.models import Product
from django.urls import reverse



class CartProduct(models.Model):
    """Продукт карзины"""
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=19, decimal_places=0, verbose_name='Общая цена')


    def __str__(self):
        return f"Продукт: {self.product.title} (для корзины)"

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт корзины'
        verbose_name_plural = 'Продукты корзины'


class Cart(models.Model):
    """Корзина"""
    owner = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart_products = models.ManyToManyField(
        CartProduct, blank=True, related_name='related_cart', verbose_name='Продукты для корзины'
    )
    total_products = models.IntegerField(default=0, verbose_name='Общее кол-во товара')
    final_price = models.DecimalField(max_digits=19, decimal_places=0, default=0, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)


    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            self.total_products = self.cart_products.count()
            self.final_price = sum([cproduct.final_price for cproduct in self.cart_products.all()])
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Order(models.Model):
    """Заказ пользователя"""
    
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOISES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ получен покупателем')
    )

    BUYING_TYPE_CHOISES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )


    customer = models.ForeignKey(
        'Customer', verbose_name='Покупатель', related_name='orders', on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOISES, default=STATUS_NEW
    )
    buying_type = models.CharField(max_length=100, verbose_name='Тип заказа', choices=BUYING_TYPE_CHOISES)
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateField(verbose_name='Дата создания заказа', auto_now=True)
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)


    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Customer(models.Model):
    """Покупатель"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_activ = models.BooleanField(default=True, verbose_name='Активный?')
    customer_orders = models.ManyToManyField(
        Order, blank=True, verbose_name='Заказы покупателя', related_name='related_customer'
    )
    wishlist = models.ManyToManyField(Product, blank=True, verbose_name='Список ожидаемого')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')


    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def get_absolute_url(self):
        return reverse('customers', kwargs={'pk': self.pk})