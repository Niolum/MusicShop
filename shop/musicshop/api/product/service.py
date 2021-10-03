from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from musicshop.api.product.models import Product


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


def get_client_ip(request):
    """Получение IP пользовтаеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    sucategory = CharFilterInFilter(field_name='subcategory__title', lookup_expr='in')
    brand = CharFilterInFilter(field_name='brand__title', lookup_expr='in')
    price = filters.RangeFilter()
    

    class Meta:
        model = Product
        fields = ['subcategory', 'brand', 'price']