from django.test import TestCase
from django.urls import reverse


class CartViewTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_cart_view_url_exists_at_desired_location(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get('/carts/')
        self.assertEqual(resp.status_code, 200)

    def test_cart_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('cart'))
        self.assertEqual(resp.status_code, 200)

    def test_cart_view_uses_correct_template(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('cart'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cart/cart.html')

    def test_add_to_cart_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('add_to_cart',  args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertRedirects(resp, '/products/fender_am_pro_ii_tele_mn_bk/')

    def test_delete_from_cart_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('add_to_cart',  args=['fender_am_pro_ii_tele_mn_bk']))
        resp1 = self.client.get(reverse('delete_from_cart',  args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertRedirects(resp1, '/carts/')

    # def test_changeQTY_cart_view_url_accessible_by_name(self):
    #     self.client.login(username='niolum', password='170498sb')
    #     resp = self.client.get(reverse('add_to_cart',  args=['fender_am_pro_ii_tele_mn_bk']), { 'qty': '1'})
    #     resp1 = self.client.post(reverse('change_qty',  args=['fender_am_pro_ii_tele_mn_bk']))
    #     self.assertRedirects(resp1, '/carts/')


class OrderViewTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_order_view_url_exists_at_desired_location(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get('/carts/ordercheck/')
        self.assertEqual(resp.status_code, 200)

    def test_order_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('ordercheck'))
        self.assertEqual(resp.status_code, 200)

    def test_order_view_uses_correct_template(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('ordercheck'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cart/ordercheck.html')

    def test_make_order(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('makeorder'), 
                                    {'customer':1, 
                                    'first_name':'Alexander', 
                                    'last_name':'Belov',
                                    'phone': '891455546879',
                                    'cart': 5,
                                    'address':'ул. Ключевская 21',
                                    'buying_type': 'self',
                                    'comment': '',
                                    'order_date': '2022-06-21'})
        self.assertRedirects(resp, '/carts/')


class WishlistViewTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_wishlist_view_url_exists_at_desired_location(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get('/carts/wishlist/')
        self.assertEqual(resp.status_code, 200)

    def test_wishlist_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('wishlist'))
        self.assertEqual(resp.status_code, 200)

    def test_wishlist_view_uses_correct_template(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('wishlist'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'cart/wishlist.html')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('wishlist'))
        self.assertRedirects(resp, '/users/accounts/login/?next=/carts/wishlist/')

    def test_add_to_wishlist_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('add_wishlist',  args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertRedirects(resp, '/products/fender_am_pro_ii_tele_mn_bk/') 

    def test_delete_from_wishlist_view_url_accessible_by_name(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('add_wishlist',  args=['fender_am_pro_ii_tele_mn_bk']))
        resp1 = self.client.get(reverse('delete_from_wishlist',  args=['fender_am_pro_ii_tele_mn_bk']))
        self.assertRedirects(resp1, '/carts/wishlist/')