import django_filters
from .models import Subcategory


class SubcategoryFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Subcategory
        fields = ['category__url']