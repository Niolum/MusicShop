from django.shortcuts import get_object_or_404, render, redirect
from cart.forms import OrderForm
from ..models import Cart, CartProduct, Customer
from product.models import Product
from ..mixins import CartMixin
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class AddToCartView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'
    
    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('url')
        product = Product.objects.get(url=product_slug)

        if request.user.is_authenticated:
            cart_product, created = CartProduct.objects.get_or_create(
                user=self.cart.owner, cart=self.cart, product=product
            )
            if created:
                self.cart.cart_products.add(cart_product)
            Cart.save(self.cart)
            messages.add_message(request,messages.INFO,'Товар добавлен в корзину')
            return redirect(product.get_absolute_url())
        

class DeleteFromCartView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('url')
        product = Product.objects.get(url=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, product=product
        )
        self.cart.cart_products.remove(cart_product)
        cart_product.delete()
        Cart.save(self.cart)
        messages.add_message(request,messages.INFO,'Товар удален из корзины')
        return HttpResponseRedirect(reverse('cart'))


class ChangeQTYView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get('url')
        product = Product.objects.get(url=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, product=product
        )
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        Cart.save(self.cart)

        messages.add_message(request,messages.INFO,'Кол-во изменено')
        return HttpResponseRedirect(reverse('cart'))


class CartView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        context = {'cart': self.cart}
        return render(request, 'cart/cart.html', context)


class OrderCheckView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'form': form
        }
        return render(request, 'cart/ordercheck.html', context)


class MakeOrderView(LoginRequiredMixin, CartMixin, View):
    login_url = 'login'

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.comment = form.cleaned_data['comment']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save
            customer.customer_orders.add(new_order)
            messages.add_message(request, messages.INFO, 'Спасибо за заказ! Менеджер с Вами свяжется')
        return HttpResponseRedirect(reverse('cart'))


class AddWishlist(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, url=self.kwargs['slug'])
        customer = Customer.objects.get(user=request.user)
        customer.wishlist.add(product)
        return redirect(product.get_absolute_url())


class DeleteFromWishlist(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, url=self.kwargs['slug'])
        customer = Customer.objects.get(user=request.user)
        customer.wishlist.remove(product)
        return HttpResponseRedirect(reverse('wishlist'))


class WishlistView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'cart/wishlist.html'
    login_url = 'login'

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(WishlistView, self).get_context_data(**kwargs)
        context['wishlist'] = context['customer_list'][0].wishlist.select_related('subcategory')
        return context