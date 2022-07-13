from django.db import models
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Category, Subcategory, Product, Brand, Rating
from ..serializers import (
    CreateRatingSerializer, 
    ProductListSerializer, 
    ProductDetailSerializer, 
    ReviewCreateSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    SubcategoryListSerializer,
    SubcategoryDetailSerializer,
)
from ..service import ProductFilter, PaginationProducts, SubcategoryFilter



#REST
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка товаров"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = PaginationProducts
    queryset = Product.objects.all()

    def get_queryset(self):
        products = Product.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings", filter=models.Q(ratings__user=self.request.user))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__value')) / models.Count(models.F('ratings'))
        )
        return products

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к товару"""
    serializer_class = ReviewCreateSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга к товару"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategorysViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод категорий"""
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        elif self.action == 'retrieve':
            return CategoryDetailSerializer


class SubcategorysViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод подкатегорий"""
    filterset_class = SubcategoryFilter
    queryset = Subcategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SubcategoryListSerializer
        elif self.action == 'retrieve':
            return SubcategoryDetailSerializer