from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from .models import Cart, Customer, CartProduct
from product.models import Product
from .serializers import CartSerializer, OrderCreateSerializer
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST


# class CartDetailView(DetailView):
#     model = Cart

#     @staticmethod
#     def get_or_create_cart(user):
#         if user.is_authenticated:
#             return Cart.objects.get_or_create(owner=user.customer, for_anonmous_user=False).first()
#         return Cart.objects.filter(for_anonymous_user=True).first()

#     @staticmethod
#     def _get_or_create_cart_product(customer: Customer, cart: Cart, product: Product):
#         cart_product, created = CartProduct.objects.get_or_create(
#             user=customer,
#             product=product,
#             cart=cart
#         )
#         return cart_product, created

#     @require_POST
#     def add_to_cart(request, product_id):
#         cart = Cart(request)
#         product = self._get_or_create_cart_product()
def add_to_cart(request, user, *args, **kwargs):
    if user.is_authenticated:
        user_cart = Cart.objects.get_or_create(owner=user.customer, for_anonymous_user=False)
    else:
        user_cart = Cart.objects.get_or_create(for_anonymous_user=True)
    product = get_object_or_404(Product, id=kwargs['product_id'])
    cart_product, created = CartProduct.objects.get_or_create(user=user.customer, product=product, cart=user_cart)
    if created:
        user_cart.cart_products.add(cart_product)
        user_cart.save()
    return render(request, 'addcart.html', {'user_cart': user_cart, 'cart_product': cart_product})
    
        



#REST
class CartViewSet(ModelViewSet):
    """Действия с корзиной"""
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    @staticmethod
    def get_cart(user):
        if user.is_authenticated:
            return Cart.objects.filter(owner=user.customer, for_anonymous_user=False).first()
        return Cart.objects.filter(for_anonymous_user=True).first()


    @staticmethod
    def _get_or_create_cart_product(customer: Customer, cart: Cart, product: Product):
        cart_product, created = CartProduct.objects.get_or_create(
            user=customer,
            product=product,
            cart=cart
        )
        return cart_product, created

    
    @action(methods=["get"], detail=False)
    def current_customer_cart(self, *args, **kwargs):
        cart = self.get_cart(self.request.user)
        cart_serializer = CartSerializer(cart)
        return Response(cart_serializer.data)

    @action(methods=["put"], detail=False, url_path='current_customer_cart/add_to_cart/(?P<product_id>\d+)')
    def product_add_to_cart(self, *args, **kwargs):
        cart = self.get_cart(self.request.user)
        product = get_object_or_404(Product, id=kwargs['product_id'])
        cart_product, created = self._get_or_create_cart_product(self.request.user.customer, cart, product)
        if created:
            cart.cart_products.add(cart_product)
            cart.save()
            return Response({"detail": "Товар добавлен в корзину", "added": True})
        return Response({"detail": "Товар уже в корзине", "added": False}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["patch"], detail=False, url_path='current_customer_cart/change_qty/(?P<qty>\d+)/(?P<cart_product_id>\d+)')
    def product_change_qty(self, *args, **kwargs):
        cart_product = get_object_or_404(CartProduct, id=kwargs['cart_product_id'])
        cart_product.qty = int(kwargs['qty'])
        cart_product.save()
        cart_product.cart.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=["put"], detail=False, url_path='current_customer_cart/remove_from_cart/(?P<cproduct_id>\d+)')
    def product_remove_from_cart(self, *args, **kwargs):
        cart = self.get_cart(user=self.request.user)
        cproduct = get_object_or_404(CartProduct, id=kwargs['cproduct_id'])
        cart.cart_products.remove(cproduct)
        cproduct.delete()
        cart.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderCreateViewSet(ModelViewSet):
    """Оформление заказа"""
    serializer_class = OrderCreateSerializer

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)