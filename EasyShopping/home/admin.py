from django.contrib import admin
from .models import Category, Product, UserInterest

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productID', 'productName', 'price', 'discount']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserInterest)