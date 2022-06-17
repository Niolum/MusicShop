from django.test import TestCase
from ..models import Category, Subcategory, Product, Brand, Review, ProductPhoto
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            title='Guitars',
            image='gi.webp',
            description='diferent guitars',
            url='guitars'
        )

    def test_title_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_title_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_image_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_image_upload_to(self):
        category = Category.objects.get(id=1)
        upload_to = category._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'category/')

    def test_description_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_url_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('url').max_length
        self.assertEquals(max_length, 160)

    def test_url_unique(self):
        category = Category.objects.get(id=1)
        unique = category._meta.get_field('url').unique
        self.assertEquals(unique, True)

    def test_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/categories/guitars/')


class SubcategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Subcategory.objects.create(
            title='Electric Guitars',
            image='electric-guitars.webp',
            description='all electric guitars',
            url='electric_guitars'
        )

    def test_title_label(self):
        subcategory = Subcategory.objects.get(id=1)
        field_label = subcategory._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_title_max_length(self):
        subcategory = Subcategory.objects.get(id=1)
        max_length = subcategory._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_image_label(self):
        subcategory = Subcategory.objects.get(id=1)
        field_label = subcategory._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_image_upload_to(self):
        subcategory = Subcategory.objects.get(id=1)
        upload_to = subcategory._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'subcategory/')

    def test_description_label(self):
        subcategory = Subcategory.objects.get(id=1)
        field_label = subcategory._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_url_label(self):
        subcategory = Subcategory.objects.get(id=1)
        field_label = subcategory._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_max_length(self):
        subcategory = Subcategory.objects.get(id=1)
        max_length = subcategory._meta.get_field('url').max_length
        self.assertEquals(max_length, 160)

    def test_url_unique(self):
        subcategory = Subcategory.objects.get(id=1)
        unique = subcategory._meta.get_field('url').unique
        self.assertEquals(unique, True)

    def test_get_absolute_url(self):
        subcategory = Subcategory.objects.get(id=1)
        self.assertEquals(subcategory.get_absolute_url(), '/subcategories/electric_guitars/')


class BrandModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(
            title='Fender',
            image='electric-guitars.webp',
            description="all Fender's products",
            url='fender'
        )

    def test_title_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_title_max_length(self):
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_image_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_image_upload_to(self):
        brand = Brand.objects.get(id=1)
        upload_to = brand._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'brand/')

    def test_description_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_url_label(self):
        brand = Brand.objects.get(id=1)
        field_label = brand._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_max_length(self):
        brand = Brand.objects.get(id=1)
        max_length = brand._meta.get_field('url').max_length
        self.assertEquals(max_length, 160)

    def test_url_unique(self):
        brand = Brand.objects.get(id=1)
        unique = brand._meta.get_field('url').unique
        self.assertEquals(unique, True)


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            title='Fender Telecaster',
            price=90000,
            description='Cool and legendary guitar',
            image='fender-tele-mn-bk1.webp',
            stock=4,
            url='tele_mn_bk1',
            draft=False
        )
    
    def test_title_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')
    
    def test_title_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Цена')
        
    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_image_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_image_upload_to(self):
        product = Product.objects.get(id=1)
        upload_to = product._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'product/')

    def test_stock_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('stock').verbose_name
        self.assertEquals(field_label, 'Наличие на складе')

    def test_stock_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('stock').default
        self.assertEquals(default, 0)

    def test_url_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('url').max_length
        self.assertEquals(max_length, 160)

    def test_url_unique(self):
        product = Product.objects.get(id=1)
        unique = product._meta.get_field('url').unique
        self.assertEquals(unique, True)

    def test_draft_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('draft').verbose_name
        self.assertEquals(field_label, 'Черновик')

    def test_draft_default(self):
        product = Product.objects.get(id=1)
        default = product._meta.get_field('draft').default
        self.assertEquals(default, False)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        self.assertEquals(product.get_absolute_url(), '/products/tele_mn_bk1/')


class ProductPhotoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(
            title='Fender Telecaster',
            price=90000,
            description='Cool and legendary guitar',
            image='fender-tele-mn-bk1.webp',
            stock=4,
            url='tele_mn_bk1',
            draft=False
        )
        ProductPhoto.objects.create(
            title='fender-tele-mn-bk',
            image='fender-tele-mn-bk.jpg',
            description="guitar fender tele-mn-bk",
            product_id=1
        )

    def test_title_label(self):
        product_photo = ProductPhoto.objects.get(id=1)
        field_label = product_photo._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')
    
    def test_title_max_length(self):
        product_photo = ProductPhoto.objects.get(id=1)
        max_length = product_photo._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_image_label(self):
        product_photo = ProductPhoto.objects.get(id=1)
        field_label = product_photo._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'Изображение')

    def test_image_upload_to(self):
        product_photo = ProductPhoto.objects.get(id=1)
        upload_to = product_photo._meta.get_field('image').upload_to
        self.assertEquals(upload_to, 'product_photo/')

    def test_description_label(self):
        product_photo = ProductPhoto.objects.get(id=1)
        field_label = product_photo._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание')


class ReviewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username="dummy",
            first_name="a",
            last_name="dummy",
            password="randompassword",
            email="test@test.com"
        )
        Product.objects.create(
            title='Fender Telecaster',
            price=90000,
            description='Cool and legendary guitar',
            image='fender-tele-mn-bk1.webp',
            stock=4,
            url='tele_mn_bk1',
            draft=False
        )
        Review.objects.create(
            user_id=1,
            text="Cool",
            product_id=1
        )

    def test_user_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'пользователь')
    
    def test_text_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Сообщение')

    def test_text_max_length(self):
        review = Review.objects.get(id=1)
        max_length = review._meta.get_field('text').max_length
        self.assertEquals(max_length, 5000)

    def test_product_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('product').verbose_name
        self.assertEquals(field_label, 'продукт')