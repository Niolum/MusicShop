from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from musicshop.api.user.serializers import UserSerializer


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'is_authenticated': True}) if request.user.is_authenticated else Response({'is_authenticated': False})
        

class UserListView(generics.ListAPIView):
    """Список юзеров"""
    queryset = User.objects.all()
    serializer_class = UserSerializer