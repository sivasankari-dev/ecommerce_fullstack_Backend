from django.contrib import admin
from .models import CustomUser, Product, Category, Cart, CartItem, Review, ProductRating, Wishlist
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name")
admin.site.register(CustomUser, CustomUserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "featured")

admin.site.register(Product, ProductAdmin)    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")

admin.site.register(Category, CategoryAdmin)    

admin.site.register([Cart, CartItem, Review, ProductRating, Wishlist])