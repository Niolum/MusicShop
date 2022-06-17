from django.test import TestCase
from django.urls import reverse


class SigninTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_login_returns_200(self):
        resp = self.client.get('/users/accounts/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/login.html')

    def test_login_and_open_profile(self):
        self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('editprofile'))
        self.assertEqual(resp.status_code, 200)

    def test_login_invalid_form(self):
        resp = self.client.post('/users/accounts/login/', {
            "username": "niolum",
            "password": "170498"
        })
        form = resp.context.get('form')
        self.assertFalse(form.is_valid())


class LogoutTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_logout(self):
        resp = self.client.get('/users/accounts/logout/')
        self.assertEqual(resp.status_code, 200)


class RegistrationTest(TestCase):

    def test_registration_view(self):
        resp = self.client.post(reverse('register'), 
                                    { 'username':'foo', 
                                    'password':'bar', 
                                    'password2':'bar' })
        self.assertTemplateUsed(resp, 'registration/register_done.html')


class EditProfileTest(TestCase):
    fixtures = ['product.json', 'user.json', 'cart.json']

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('editprofile'))
        self.assertRedirects(resp, '/users/accounts/login/?next=/users/editprofile/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='niolum', password='170498sb')
        resp = self.client.get(reverse('editprofile'))
        self.assertEqual(str(resp.context['user']), 'niolum')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'registration/editprofile.html')