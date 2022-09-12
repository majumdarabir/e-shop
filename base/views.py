from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm


def register_user(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            messages.success(request, 'Successfully logged in !!')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
            return redirect('register')
    else:
        form = RegistrationForm
        return render(request, 'base/register.html', {'form': form})


def login_user(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form: AuthenticationForm = AuthenticationForm(request.POST)
        user_info = {
            "username": request.POST.get("username"),
            "password": request.POST.get('password')
        }
        user = authenticate(request, **user_info)
        if user:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('home')
        else:
            messages.warning(request, f'Some problem {user_info}')
            return redirect('login')
    else:
        form = AuthenticationForm
        return render(request, 'base/signin.html', {'form': form})


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, "Successfully logger out ")
    return redirect("home")
