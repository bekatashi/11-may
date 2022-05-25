from django.contrib import admin
from .models import Product, Category, NewProduct

admin.site.register(Product)
admin.site.register(NewProduct)
admin.site.register(Category)
