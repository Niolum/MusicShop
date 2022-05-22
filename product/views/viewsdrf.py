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
from ..service import ProductFilter, PaginationProducts



#REST
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка товаров"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = PaginationProducts
    queryset = Product.objects.all()

    # def get_queryset(self):
    #     products = Product.objects.filter(draft=False).annotate(
    #         rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
    #     ).annotate(
    #         middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
    #     )
    #     return products

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

    # def perform_create(self, serializer):
    #     serializer.save(ip=get_client_ip(self.request))


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
    queryset = Subcategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SubcategoryListSerializer
        elif self.action == 'retrieve':
            return SubcategoryDetailSerializer