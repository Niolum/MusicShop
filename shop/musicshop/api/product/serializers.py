from rest_framework import serializers
from musicshop.api.product.models import Category, Subcategory, Product, Rating, Review


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
    middle_star = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'brand', 'price', 'subcategory', 'rating_user', 'middle_star']


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = ['id', 'email', 'name', 'text', 'parent', 'product']


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзывов"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ['name', 'text', 'children']


class ProductDetailSerializer(serializers.ModelSerializer):
    """Полное описание товара"""
    subcategory = SubcategoryListSerializer(read_only=True)
    brand = serializers.SlugRelatedField(slug_field="title", read_only=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        exclude = ['draft']


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ['star', 'product']

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            product=validated_data.get('product', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating