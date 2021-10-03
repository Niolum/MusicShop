from .models import Cart, CartProduct, Category, Customer, Subcategory, Product, Brand, Review, Order
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib import auth


# Create your tests here.

class ShopTests(APITestCase):

    def setUp(self):
        self.one_category = Category.objects.create(title='Guitars', image='guitar.jpg', description='All guitars', url='guitars')
        self.two_category = Category.objects.create(title='Drums', image='drum.jpg', description='All drums', url='drums')

        self.one_subcategory = Subcategory.objects.create(
            title='Electric Guitars', 
            image='elecguitar.jpg', 
            description='All electricguitars', 
            url='electric_guitars', 
            category=Category.objects.get(id=1)
        )
        self.two_subcategory = Subcategory.objects.create(
            title='Basses', 
            image='bass.jpg', 
            description='All basses', 
            url='bass', 
            category=Category.objects.get(id=1)
        )

        self.one_brand = Brand.objects.create(
            title='Fender', 
            image='fender.jpg', 
            description='fender brand', 
            url='fender'
        )

        self.two_brand = Brand.objects.create(
            title='Gibson', 
            image='gibson.jpg', 
            description='gibson brand', 
            url='gibson'
        )

        self.one_product = Product.objects.create(
            title='Gibson SG 2019', 
            price=20000,
            description='gibson brand',
            image='SG2019.jpg',
            stock=4,
            subcategory=Subcategory.objects.get(id=1),
            brand=Brand.objects.get(id=2),
            url='gibson_sg_2019',
            draft=False
        )

        self.two_product = Product.objects.create(
            title='Gibson LP 2019', 
            price=25000,
            description='gibson brand',
            image='LP2019.jpg',
            stock=3,
            subcategory=Subcategory.objects.get(id=1),
            brand=Brand.objects.get(id=2),
            url='gibson_LP_2019',
            draft=True
        )

        self.review = Review.objects.create(
            email = 'Mark@mail.ru',
            name = 'Mark',
            text = 'good guitar',
            parent = None,
            product = Product.objects.get(id=1)
        )

    def test_product_list(self):
        # Проверка списка продуктов
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 2)
        print(response.data)


    def test_product_zdetail(self):
        # Проверка информации об одном продукте
        response = self.client.get(reverse('product-detail', args=(self.one_product.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


    def test_category_list(self):
        # Проверка списка категорий
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 2)
        print(response.data)


    def test_category_zdetail(self):
        # Проверка информации об одной категории
        response = self.client.get(reverse('category-detail', args=(self.one_category.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


    def test_subcategory_list(self):
        # Проверка списка подкатегорий
        response = self.client.get(reverse('subcategory-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subcategory.objects.count(), 2)
        print(response.data)


    def test_subcategory_zdetail(self):
        # Проверка информации об одной подкатегории
        response = self.client.get(reverse('subcategory-detail', args=(self.one_subcategory.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)


class UserTests(APITestCase):

    def setUp(self):
        new_user1_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }

        self.new_user1 = User.objects.create_user(
            username=new_user1_data["username"],
            first_name=new_user1_data["first_name"],
            last_name=new_user1_data["last_name"],
            email=new_user1_data["email"],
            password=new_user1_data["password"]
        )


    def test_login_and_logout(self):
        """
        тест на вход и выход пользователя
        """
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print("[!] Login failed!")
        user = auth.get_user(self.client)
        print("user: ", user)
        print(User.objects.all())

        self.client.logout()
        user = auth.get_user(self.client)
        print("user: ", user)



class CartTests(APITestCase):

    def setUp(self):
        new_user_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }

        self.new_user = User.objects.create_user(
            username=new_user_data["username"],
            first_name=new_user_data["first_name"],
            last_name=new_user_data["last_name"],
            email=new_user_data["email"],
            password=new_user_data["password"]
        )

        self.one_customer = Customer.objects.create(
            user = self.new_user,
            is_activ = True,
            phone = "",
            address = ""
        )
        
        self.one_cart = Cart.objects.create(
            owner = self.one_customer,
            total_products = 0,
            final_price = 0,
            in_order = False,
            for_anonymous_user = False
        )
        self.one_cart.save()
        self.one_cart.cart_products.set([],)

        self.one_order = Order.objects.create(
            customer = self.one_customer,
            first_name = "dummy",
            last_name = "crivie",
            phone = "+7898879876",
            cart = self.one_cart,
            address = "Russia",
            status = "STATUS_NEW",
            buying_type = "BUYING_TYPE_SELF",
            comment = ""
        )
        
        self.one_customer.customer_orders.set([self.one_order],)
        self.one_customer.wishlist.set([],)

        self.one_category = Category.objects.create(title='Guitars', image='guitar.jpg', description='All guitars', url='guitars')
        self.two_category = Category.objects.create(title='Drums', image='drum.jpg', description='All drums', url='drums')
 
        self.one_subcategory = Subcategory.objects.create(
            title='Electric Guitars', 
            image='elecguitar.jpg', 
            description='All electricguitars', 
            url='electric_guitars', 
            category=Category.objects.get(id=1)
        )
        self.two_subcategory = Subcategory.objects.create(
            title='Basses', 
            image='bass.jpg', 
            description='All basses', 
            url='bass', 
            category=Category.objects.get(id=1)
        )

        self.one_brand = Brand.objects.create(
            title='Fender', 
            image='fender.jpg', 
            description='fender brand', 
            url='fender'
        )

        self.two_brand = Brand.objects.create(
            title='Gibson', 
            image='gibson.jpg', 
            description='gibson brand', 
            url='gibson'
        )

        self.one_product = Product.objects.create(
            title='Gibson SG 2019', 
            price=20000,
            description='gibson brand',
            image='SG2019.jpg',
            stock=4,
            subcategory=Subcategory.objects.get(id=1),
            brand=Brand.objects.get(id=2),
            url='gibson_sg_2019',
            draft=False
        )

        self.two_product = Product.objects.create(
            title='Gibson LP 2019', 
            price=25000,
            description='gibson brand',
            image='LP2019.jpg',
            stock=3,
            subcategory=Subcategory.objects.get(id=1),
            brand=Brand.objects.get(id=2),
            url='gibson_LP_2019',
            draft=True
        )


    def test_get_list_cart(self): 
        # Проверка списка корзина
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cart.objects.count(), 1)
        print(response.data)


    def test_get_current_customer_cart(self):
        # Проверка корзины текущего юзера
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print("[!] Login failed!")
        user = auth.get_user(self.client)
        print("user: ", user)
        response = self.client.get(reverse('cart-current-customer-cart'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cart.objects.count(), 1)
        print(response.data)

    def test_add_to_cart(self):
        # Проверка на добавление продукта в корзину
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
        # добавление в корзину
        url = reverse('cart-product-add-to-cart', args=['1'])
        data = {'title': 'Gibson SG 2019', 
            'price': 20000,
            'description': 'gibson brand',
            'image': 'SG2019.jpg',
            'stock': 4,
            'subcategory': 'Electric Guitars',
            'brand': 'Gibson',
            'url': 'gibson_sg_2019',
            'draft': False}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CartProduct.objects.count(), 1)
        print(response.data)


        # изменение количества товаров в корзине
        url = reverse('cart-product-change-qty', args=['2', '1'])
        data = {'title': 'Gibson SG 2019', 
            'price': 20000,
            'description': 'gibson brand',
            'image': 'SG2019.jpg',
            'stock': 4,
            'subcategory': 'Electric Guitars',
            'brand': 'Gibson',
            'url': 'gibson_sg_2019',
            'draft': False}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response2 = self.client.get(reverse('cart-current-customer-cart'))
        print(response2.data)


        #  Удаление из корзины
        url = reverse('cart-product-remove-from-cart', args=['1'])
        data = {'title': 'Gibson SG 2019', 
            'price': 20000,
            'description': 'gibson brand',
            'image': 'SG2019.jpg',
            'stock': 4,
            'subcategory': 'Electric Guitars',
            'brand': 'Gibson',
            'url': 'gibson_sg_2019',
            'draft': False}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CartProduct.objects.count(), 0)


class OrderTests(APITestCase):

    def setUp(self):
        new_user_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }

        self.new_user = User.objects.create_user(
            username=new_user_data["username"],
            first_name=new_user_data["first_name"],
            last_name=new_user_data["last_name"],
            email=new_user_data["email"],
            password=new_user_data["password"]
        )

        self.one_customer = Customer.objects.create(
            user = self.new_user,
            is_activ = True,
            phone = "",
            address = ""
        )
        
        self.one_cart = Cart.objects.create(
            owner = self.one_customer,
            total_products = 0,
            final_price = 0,
            in_order = False,
            for_anonymous_user = False
        )
        
        self.one_customer.customer_orders.set([],)
        self.one_customer.wishlist.set([],)

        self.one_category = Category.objects.create(title='Guitars', image='guitar.jpg', description='All guitars', url='guitars')
        self.two_category = Category.objects.create(title='Drums', image='drum.jpg', description='All drums', url='drums')
 
        self.one_subcategory = Subcategory.objects.create(
            title='Electric Guitars', 
            image='elecguitar.jpg', 
            description='All electricguitars', 
            url='electric_guitars', 
            category=Category.objects.get(id=1)
        )
        self.two_subcategory = Subcategory.objects.create(
            title='Basses', 
            image='bass.jpg', 
            description='All basses', 
            url='bass', 
            category=Category.objects.get(id=1)
        )

        self.one_brand = Brand.objects.create(
            title = 'Fender', 
            image = 'fender.jpg', 
            description = 'fender brand', 
            url = 'fender'
        )

        self.two_brand = Brand.objects.create(
            title = 'Gibson', 
            image = 'gibson.jpg', 
            description = 'gibson brand', 
            url = 'gibson'
        )

        self.one_product = Product.objects.create(
            title = 'Gibson SG 2019', 
            price = 20000,
            description = 'gibson brand',
            image = 'SG2019.jpg',
            stock = 4,
            subcategory = Subcategory.objects.get(id=1),
            brand = Brand.objects.get(id=2),
            url = 'gibson_sg_2019',
            draft = False
        )

        self.two_product = Product.objects.create(
            title = 'Gibson LP 2019', 
            price = 25000,
            description = 'gibson brand',
            image = 'LP2019.jpg',
            stock = 3,
            subcategory = Subcategory.objects.get(id=1),
            brand = Brand.objects.get(id=2),
            url  ='gibson_LP_2019',
            draft = True
        )

        self.one_cartproduct = CartProduct.objects.create(
            user = self.one_customer,
            cart = self.one_cart,
            product = self.one_product,
            qty = 1,
            final_price = 20000
        )
        self.one_cart.cart_products.set([CartProduct.objects.get(id=1)],)
        self.one_cart.save()


    def test_create_order(self):
        # Проверка на создание заказа
        url = reverse('order')
        data = {'customer': 1,
            'first_name': 'dummy',
            'last_name': 'crivie',
            'phone': '+7898879876',
            'cart': 1,
            'address': 'Russia',
            'buying_type': 'self',
            'order_date': '2021-10-14'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        print(response.data)

