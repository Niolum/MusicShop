from django.urls import path, include
from user.views.views import login, logout, register, editprofile



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login),
    path('accounts/logout/', logout),
    path('register/', register, name='register'),
    path('editprofile/', editprofile, name='editprofile')
]