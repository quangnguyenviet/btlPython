from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random
from home import models

# Create your views here.
class ProductDetailView(View):
    def get(self, request, **kwargs):
        product = models.Product.objects.filter(productID = int(kwargs.get('id')))
        product = product[0]
        # relatedProduct = models.Product.objects.filter(category = product.category)
        # se = set()
        # for i in range(len(relatedProduct)):
        #     randIndex = random.randint(0)
            
        # print(relatedProduct)
        context = {
            "product" : product,
            'message' : "hello"
        }
        return render(request, 'productdetail/index.html', context)