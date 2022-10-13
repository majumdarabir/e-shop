from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import ChangePasswordForm, RegistrationForm, UpgradeCustomerForm


def register_user(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Successfully logged in !!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            return redirect('register')
    form = RegistrationForm
    return render(request, 'base/register.html', {'form': form})


def login_user(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_info = {
                "username": form.data.get("username"),
                "password": form.data.get('password')
            }
            user = authenticate(request, **user_info)
            if user:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
            else:
                messages.warning(request, f'Some problem {user_info}')
            return redirect('login')
        messages.warning(request, form.errors)
        return redirect("login")
    form = AuthenticationForm
    return render(request, 'base/signin.html', {'form': form})


@login_required
def change_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            user = request.user
            old_password = change_password_form.cleaned_data.get(
                "old_password")
            new_password = change_password_form.cleaned_data.get(
                "new_password")
            if not user.check_password(old_password):
                messages.warning(request, f"{user} has a different password")
                return redirect("login")
            user.set_password(new_password)
            user.save()
            messages.success(request, f"changed password for {user}")
        else:
            messages.warning(request, change_password_form.errors)
    return redirect("profile")


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        profile_form = UpgradeCustomerForm(
            request.POST, request.FILES, instance=request.user.customer)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Updated your profile")
        else:
            messages.error(request, profile_form.errors)
        return redirect("profile")
    change_profile_form = UpgradeCustomerForm(instance=request.user.customer)
    change_password_form = ChangePasswordForm
    return render(request, "base/profile_details.html",
                  {"change_password": change_password_form, "upgrade": change_profile_form})


@login_required
def delete_account(request: HttpRequest) -> HttpResponse:
    if request.user.delete():
        messages.success(request, "User deleted successfully")
    else:
        messages.warning(request, "Failed to delete the user")
    return redirect("login")


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, "Successfully logger out ")
    return redirect("login")
