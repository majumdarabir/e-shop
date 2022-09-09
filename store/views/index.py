from store.models.product import Product
from store.models.customer import Customer
from store.models.category import Category
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class Index(View):
    def index(self, request):
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
