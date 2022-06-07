from .models import Category, Subcategory, Product, Brand, Review
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

        # self.review = Review.objects.create(
        #     email = 'Mark@mail.ru',
        #     name = 'Mark',
        #     text = 'good guitar',
        #     parent = None,
        #     product = Product.objects.get(id=1)
        # )

    def test_product_list(self):
        # Проверка списка продуктов
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 2)
        


    def test_product_zdetail(self):
        # Проверка информации об одном продукте
        response = self.client.get(reverse('product-detail', args=(self.one_product.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


    def test_category_list(self):
        # Проверка списка категорий
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 2)
        


    def test_category_zdetail(self):
        # Проверка информации об одной категории
        response = self.client.get(reverse('category-detail', args=(self.one_category.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        


    def test_subcategory_list(self):
        # Проверка списка подкатегорий
        response = self.client.get(reverse('subcategory-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subcategory.objects.count(), 2)
        


    def test_subcategory_zdetail(self):
        # Проверка информации об одной подкатегории
        response = self.client.get(reverse('subcategory-detail', args=(self.one_subcategory.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)