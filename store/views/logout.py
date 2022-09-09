from distutils.log import error
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.views import View


def logout(request):
    request.session.clear()
    redirect('login')
