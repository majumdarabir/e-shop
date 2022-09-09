from distutils.log import error
from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models import Product
from store.models import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.views import View
# Create your views here.


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'email': email

        }
        error_message = None
        customer = Customer(first_name=first_name, last_name=last_name,
                            mobile=mobile, email=email, password=password)
        error_message = self.valid(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def valid(customer):
        error_message = None
        spacialchar = '@'
        if not customer.password:
            error_message = 'Password Required'
        elif customer.password:
            if len(customer.password) < 6:
                error_message = 'Password must contain 6 digits'
            else:
                if not spacialchar in customer.password:
                    error_message = 'Password must contain special charector'
        if not customer.mobile:
            error_message = 'Mobile Number Required'
        elif customer.mobile:
            if len(customer.mobile) < 10:
                error_message = 'Mobile Number must be 10 digits long'
        if not customer.last_name:
            error_message = 'Last Name Required'
        elif customer.last_name:
            if len(customer.last_name) < 4:
                customer.error_message = 'Last Name must be 4 char long'
        if not customer.first_name:
            error_message = "First Name Required"
        elif customer.first_name:
            if len(customer.first_name) < 4:
                customer.error_message = 'First Name must be 4 char long'
        return error_message
