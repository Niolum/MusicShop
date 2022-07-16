from django.db import models
from django.urls import reverse
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):
    """Виды инструментов"""
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to="category/")
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('categories', kwargs={"slug":self.url})


class Subcategory(models.Model):
    """Подвид и комплектующие"""
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to="subcategory/")
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def get_absolute_url(self):
        return reverse('subcategories', kwargs={"slug":self.url})


class Brand(models.Model):
    """Фирмы изготовители"""
    title = models.CharField("Название", max_length=100)
    image = models.ImageField("Изображение", upload_to="brand/")
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'


class Product(models.Model):
    title = models.CharField("Название", max_length=250)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="product/")
    stock = models.SmallIntegerField("Наличие на складе", default=0)
    subcategory = models.ForeignKey(Subcategory,  verbose_name="Подкатегория", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Фирма", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)


    def __str__(self):
        return f"{self.id}-{self.brand.title}-{self.title}"

    def get_absolute_url(self):
        return reverse('products', kwargs={"slug":self.url})

    def get_review(self):
        return self.reviews.filter(parent__isnull=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPhoto(models.Model):
    """Фото товара"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="product_photo/", null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'


class Rating(models.Model):
    """ Рейтинг """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт", related_name="ratings")
    value = models.FloatField("Значение", default=0, validators=[MinValueValidator(1.0),MaxValueValidator(5.0)])
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.value}-{self.product}"

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    """ Отзывы"""
    user = models.ForeignKey(User,verbose_name='пользователь', on_delete=models.CASCADE, null=True)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children")
    product = models.ForeignKey(Product, verbose_name="продукт", on_delete=models.CASCADE, related_name="reviews")


    def __str__(self):
        return f"{self.user}-{self.text}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'