from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserAPIView, UserListView



urlpatterns = format_suffix_patterns ([
    path('rest-auth/', include('rest_auth.urls'), name='auth'),
    path('rest-auth/registration/', include('rest_auth.registration.urls'), name='registration'),
    path('is_auth/', UserAPIView.as_view(), name='user'),
    path('users/', UserListView.as_view(), name='users'),
])