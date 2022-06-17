from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from ..forms import RegistrationForm, UserEditForm
from cart.models import Customer
from cart.forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse


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


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Customer.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required(login_url='/users/accounts/login/')
def editprofile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = CustomerForm(instance=request.user.customer, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse("editprofile"))
        else:
            messages.error(request, 'Ошибка при обновлении вашего профиля')
            return HttpResponseRedirect(reverse("editprofile"))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = CustomerForm(instance=request.user.customer)
        return render(request,
                        'registration/editprofile.html',
                        {'user_form': user_form,
                        'profile_form': profile_form})
