from rest_framework import serializers
from musicshop.api.cart.models import CartProduct, Customer, Cart, Order
from musicshop.api.product.serializers import ProductDetailSerializer


class CartProductSerializer(serializers.ModelSerializer):
    """Продукт корзины"""
    product = ProductDetailSerializer()

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'qty', 'final_price']


class CustomerSerializer(serializers.ModelSerializer):
    """Покупатель"""
    user = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['id', 'user', 'is_activ', 'customer_orders', 'wishlist', 'phone', 'address']

    @staticmethod
    def get_user(obj):
        return obj.user.username if not (obj.user.first_name and obj.user.last_name) else ' '.join([obj.user.first_name, obj.user.last_name])


class CartSerializer(serializers.ModelSerializer):
    """Корзина"""
    cart_products = CartProductSerializer(many=True, read_only=True)
    owner = CustomerSerializer()

    class Meta:
        model = Cart
        fields = [
            'id', 
            'owner', 
            'cart_products', 
            'total_products',  
            'final_price', 
            'in_order', 
            'for_anonymous_user'
        ]


class OrderCreateSerializer(serializers.ModelSerializer):
    """Заказы пользователя"""

    class Meta:
        model = Order
        fields = [
            'id', 
            'customer', 
            'first_name', 
            'last_name', 
            'phone', 
            'cart', 
            'address', 
            'status', 
            'buying_type', 
            'comment', 
            'created_at', 
            'order_date'
        ]
