from distutils.log import error
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.views import View


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'signin.html')

    def post(self, request):
        error_message = None
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')
        customer = Customer.get_customer_by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                if login.return_url:
                    return HttpResponseRedirect('homepage')
                else:
                    login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Incorrect Password'
        else:
            error_message = 'No Account With This Mail'
        return render(request, 'signin.html', {'error': error_message})
