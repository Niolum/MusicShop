from django.contrib import auth
from django.http import HttpResponseRedirect


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("categories/")
    else:
        return HttpResponseRedirect("accounts/invalid/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login/")


