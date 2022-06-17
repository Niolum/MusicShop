from django.contrib.auth.models import User
from django.test import TestCase
from cart.models import Customer
from django.urls import reverse


class RegistrationFormTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_registration_form(self):
        user_count = User.objects.count()
        resp = self.client.post(reverse('register'), 
                                    {'username':'foo',
                                    'first_name':'', 
                                    'last_name': '',
                                    'password':'bar', 
                                    'password2':'bar'})
        self.assertTemplateUsed(resp, 'registration/register_done.html')
        self.assertEqual(User.objects.count(), user_count+1)
        self.assertTrue(User.objects.filter(username='foo'))


class UserCustomerFormTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='niolum', password='170498sb')
        resp = self.client.post(reverse('editprofile'),
                                    {'username':'niolumnew',
                                    'first_name':'', 
                                    'last_name': '',
                                    'email': '',
                                    'phone': '891412345678',
                                    'address': ''})
        self.assertTrue(User.objects.filter(username='niolumnew'))
        self.assertTrue(Customer.objects.filter(phone='891412345678'))