# Generated by Django 3.2.7 on 2022-02-11 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='brand/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Фирма',
                'verbose_name_plural': 'Фирмы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='category/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Изображение')),
                ('stock', models.SmallIntegerField(default=0, verbose_name='Наличие на складе')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.brand', verbose_name='Фирма')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Ratingstar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='subcategory/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='product.review', verbose_name='Родитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адресс')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='product.product', verbose_name='продукт')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_photo/', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Фото продукта',
                'verbose_name_plural': 'Фото продуктов',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.subcategory', verbose_name='Подкатегория'),
        ),
    ]
