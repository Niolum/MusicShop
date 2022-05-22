from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from product.views.viewsdrf import (
    ProductViewSet, 
    CategorysViewSet, 
    SubcategorysViewSet, 
    AddStarRatingViewSet, 
    ReviewCreateViewSet, 
)



router_product = SimpleRouter()
router_product.register('product', ProductViewSet, basename='product')
router_product.register('category', CategorysViewSet, basename='category')
router_product.register('subcategory', SubcategorysViewSet, basename='subcategory')


urlpatterns = format_suffix_patterns ([
    path('', include(router_product.urls)),
    path('review/', ReviewCreateViewSet.as_view({'post': 'create'})),
    path('rating/', AddStarRatingViewSet.as_view({'post': 'create'})),
])