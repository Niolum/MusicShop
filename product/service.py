from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Product, Subcategory


class PaginationProducts(PageNumberPagination):
    page_size = 4
    max_page_size = 1000


    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    subcategory = CharFilterInFilter(field_name='subcategory__title', lookup_expr='in')
    brand = CharFilterInFilter(field_name='brand__title', lookup_expr='in')
    price = filters.RangeFilter()
    

    class Meta:
        model = Product
        fields = ['subcategory', 'brand', 'price']


class SubcategoryFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Subcategory
        fields = ['category__url']