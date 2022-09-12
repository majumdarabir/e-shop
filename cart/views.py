from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def cart(request: HttpRequest) -> HttpResponse:
    return render(request, "")


def orders(request: HttpRequest) -> HttpResponse:
    return render(request, "")
