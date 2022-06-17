from django.test import TestCase
from ..models import Order
from django.urls import reverse


class OrderCreateFormTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_cteate_order(self):
        order_count = Order.objects.count()
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
        self.assertEqual(Order.objects.count(), order_count+1)
        self.assertTrue(Order.objects.filter(customer=1, 
                                    first_name='Alexander', 
                                    last_name='Belov',
                                    phone='891455546879',
                                    address='ул. Ключевская 21',
                                    buying_type='self',
                                    comment='',
                                    order_date='2022-06-21'))