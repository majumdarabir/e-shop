from distutils.log import error
from http.client import HTTPS_PORT
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    # return render(request, 'orders/orders.html')
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')

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
            elif mobile:
                if len(customer.mobile) < 10:
                    error_message = 'Mobile Number must be 10 digits long'
            if not customer.last_name:
                error_message = 'Last Name Required'
            elif customer.last_name:
                if len(customer.last_name) < 4:
                    customer.error_message = 'Last Name must be 4 char long'
            if not first_name:
                error_message = "First Name Required"
            elif customer.first_name:
                if len(first_name) < 4:
                    customer.error_message = 'First Name must be 4 char long'
            if customer.isExists():
                error_message = 'Email Addrress Already Registered'
            return error_message

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile': mobile,
            'email': email

        }
    customer = Customer(first_name=first_name, last_name=last_name,
                        mobile=mobile, email=email, password=password)
    error_message = valid(customer)
    if not error_message:
        customer.password = make_password(customer.password)
        customer.register()
        return render(request, 'signupsuccess.html')

    else:
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'signup.html', data)


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return render(request, 'index.html')
            else:
                error_message = 'email or password is invalid !'
        else:
            error_message = 'email or password invalid !'
        return render(request, 'index.html', {error: error_message})
