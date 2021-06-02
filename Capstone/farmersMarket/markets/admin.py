from django.contrib import admin
from .models import Market, ProductCategory, Product, Shopper, Grower

admin.site.register(Market)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Shopper)
admin.site.register(Grower)