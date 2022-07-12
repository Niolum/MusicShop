from rest_framework import serializers
from .models import Category, Subcategory, Product, Rating, Review


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parent"""
    def to_representation(self, data):
        data =data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.ModelSerializer):
    """Вывод списка категорий"""
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания категории"""
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'description', 'url']


class SubcategoryListSerializer(serializers.ModelSerializer):
    """Вывод списка подкатегорий"""
    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'category', 'image']


class SubcategoryDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описания подкатегории"""
    category = CategoryListSerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = ['id', 'title', 'category', 'image', 'description', 'url']


class ProductListSerializer(serializers.ModelSerializer):
    """Список товаров"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.FloatField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'brand', 'price', 'subcategory', 'rating_user', 'middle_star']



class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'parent', 'product']


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ['user', 'text', 'children']


class ProductDetailSerializer(serializers.ModelSerializer):
    """Полное описание товара"""
    subcategory = SubcategoryListSerializer(read_only=True)
    brand = serializers.SlugRelatedField(slug_field="title", read_only=True)
    reviews = ReviewSerializer(read_only=True, many=True)
    rating_user = serializers.BooleanField()
    middle_star = serializers.FloatField()

    class Meta:
        model = Product
        exclude = ['draft']


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ['value', 'product']

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            user=validated_data.get('user', None),
            product=validated_data.get('product', None),
            defaults={'value': validated_data.get("value")}
        )
        return rating