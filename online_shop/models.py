

from django.db import models
from .models import models

class Category(models.Model):
    title = models.CharField(max_length=25, unique=True)

    def str(self):
        return self.title

class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)
    rating = models.PositiveIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero)
    discount = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def str(self):
        return self.name

from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class Category(models.Model):
    list_display = ('title',)

@admin.register(Product)
class ProductAdmin(models.Model:
    list_display = ('name', 'category', 'price', 'quantity', 'rating', 'discount', 'created_at', 'updated_at')
    list_filter = ('category', 'rating')
    search_fields = ('name', 'description')
