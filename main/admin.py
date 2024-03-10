from django.contrib import admin
from main.models import Product, Category, ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Category)
