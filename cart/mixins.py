from django.views import View
from .models import Cart, Customer


class CartMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(user=request.user)
            cart = Cart.objects.filter(owner=customer, in_order=False).prefetch_related('cart_products').first()
            if not cart:
                cart = Cart.objects.create(owner=customer)
            self.cart=cart
            self.cart.save()
            return super().dispatch(request, *args, **kwargs)