from django.urls import path, include
from user.views.views import login, logout



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', login),
    path('accounts/logout/', logout)
]