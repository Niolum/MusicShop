from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CartViewSet, OrderCreateViewSet



router_cart = SimpleRouter()
router_cart.register('cart', CartViewSet, basename='cart')


urlpatterns = format_suffix_patterns ([
    path('', include(router_cart.urls)),
    path('order/', OrderCreateViewSet.as_view({'post': 'create'}), name='order'),
])