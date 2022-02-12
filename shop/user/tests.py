from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib import auth

# Create your tests here.
class UserTests(APITestCase):

    def setUp(self):
        new_user1_data = {
            "username": "dummy",
            "first_name": "a",
            "last_name": "dummy",
            "password": "randompassword",
            "email": "test@test.com",
        }

        self.new_user1 = User.objects.create_user(
            username=new_user1_data["username"],
            first_name=new_user1_data["first_name"],
            last_name=new_user1_data["last_name"],
            email=new_user1_data["email"],
            password=new_user1_data["password"]
        )


    def test_login_and_logout(self):
        """
        тест на вход и выход пользователя
        """
        login_response = self.client.login(
            username="dummy", password="randompassword")
        if login_response is True:
            url = reverse("users")
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            print("[!] Login failed!")
        user = auth.get_user(self.client)
        print("user: ", user)
        print(User.objects.all())

        self.client.logout()
        user = auth.get_user(self.client)
        print("user: ", user)