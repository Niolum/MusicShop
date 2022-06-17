from django.test import TestCase
from ..models import Cart, CartProduct, Customer, Order


class CartProductModelTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_user_label(self):
        cart_product = CartProduct.objects.get(id=7)
        field_label = cart_product._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Покупатель')

    def test_cart_label(self):
        cart_product = CartProduct.objects.get(id=7)
        field_label = cart_product._meta.get_field('cart').verbose_name
        self.assertEquals(field_label, 'Корзина')

    def test_product_label(self):
        cart_product = CartProduct.objects.get(id=7)
        field_label = cart_product._meta.get_field('product').verbose_name
        self.assertEquals(field_label, 'Продукт')

    def test_qty_default(self):
        cart_product = CartProduct.objects.get(id=7)
        default = cart_product._meta.get_field('qty').default
        self.assertEquals(default, 1)

    def test_final_price_label(self):
        cart_product = CartProduct.objects.get(id=7)
        field_label = cart_product._meta.get_field('final_price').verbose_name
        self.assertEquals(field_label, 'Общая цена')
        
    def test_final_price_max_digits(self):
        cart_product = CartProduct.objects.get(id=7)
        max_digits = cart_product._meta.get_field('final_price').max_digits
        self.assertEquals(max_digits, 19)


class CartModelTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_owner_label(self):
        cart = Cart.objects.get(id=1)
        field_label = cart._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'Покупатель')

    def test_cart_products_label(self):
        cart = Cart.objects.get(id=1)
        field_label = cart._meta.get_field('cart_products').verbose_name
        self.assertEquals(field_label, 'Продукты для корзины')

    def test_total_products_label(self):
        cart = Cart.objects.get(id=1)
        field_label = cart._meta.get_field('total_products').verbose_name
        self.assertEquals(field_label, 'Общее кол-во товара')

    def test_total_products_default(self):
        cart = Cart.objects.get(id=1)
        default = cart._meta.get_field('total_products').default
        self.assertEquals(default, 0)

    def test_final_price_label(self):
        cart = Cart.objects.get(id=1)
        field_label = cart._meta.get_field('final_price').verbose_name
        self.assertEquals(field_label, 'Общая цена')
        
    def test_final_price_max_digits(self):
        cart = Cart.objects.get(id=1)
        max_digits = cart._meta.get_field('final_price').max_digits
        self.assertEquals(max_digits, 19)

    def test_in_order_default(self):
        cart = Cart.objects.get(id=1)
        default = cart._meta.get_field('in_order').default
        self.assertEquals(default, False)

    def test_for_anonymous_user_default(self):
        cart = Cart.objects.get(id=1)
        default = cart._meta.get_field('for_anonymous_user').default
        self.assertEquals(default, False)


class OrderModelTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_customer_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('customer').verbose_name
        self.assertEquals(field_label, 'Покупатель')

    def test_first_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_first_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 255)

    def test_last_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_last_name_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 255)

    def test_phone_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Телефон')

    def test_phone_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)

    def test_cart_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('cart').verbose_name
        self.assertEquals(field_label, 'Корзина')

    def test_address_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'Адрес')

    def test_address_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('address').max_length
        self.assertEquals(max_length, 1024)

    def test_status_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'Статус заказа')

    def test_status_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('status').max_length
        self.assertEquals(max_length, 100)

    def test_buying_type_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('buying_type').verbose_name
        self.assertEquals(field_label, 'Тип заказа')

    def test_buying_type_max_length(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('buying_type').max_length
        self.assertEquals(max_length, 100)

    def test_comment_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('comment').verbose_name
        self.assertEquals(field_label, 'Комментарий к заказу')

    def test_created_at_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'Дата создания заказа')

    def test_order_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_date').verbose_name
        self.assertEquals(field_label, 'Дата получения заказа')


class CustomerModelTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_user_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'Пользователь')

    def test_is_activ_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('is_activ').verbose_name
        self.assertEquals(field_label, 'Активный?')

    def test_is_activ_default(self):
        customer = Customer.objects.get(id=1)
        default = customer._meta.get_field('is_activ').default
        self.assertEquals(default, True)

    def test_customer_orders_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('customer_orders').verbose_name
        self.assertEquals(field_label, 'Заказы покупателя')

    def test_wishlist_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('wishlist').verbose_name
        self.assertEquals(field_label, 'Список ожидаемого')

    def test_phone_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Номер телефона')

    def test_phone_max_length(self):
        customer = Customer.objects.get(id=1)
        max_length = customer._meta.get_field('phone').max_length
        self.assertEquals(max_length, 20)

    def test_address_label(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'Адрес')