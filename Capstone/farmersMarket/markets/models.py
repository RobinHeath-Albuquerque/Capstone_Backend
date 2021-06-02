from django.db import models
from django.contrib.auth.models import User


class Market(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Shopper(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product_category = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

        def __str__(self):
            return self.product_category


class Product(models.Model):
    name = models.CharField(max_length=50)
    product_category = models.ForeignKey(ProductCategory, default=1, verbose_name="Category",
                                         on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


class Grower(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=80)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    product = models.ForeignKey(Product, default=1, verbose_name="Category",
                                on_delete=models.SET_DEFAULT)
    market = models.ForeignKey(Market, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name
