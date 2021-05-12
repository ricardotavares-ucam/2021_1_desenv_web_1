from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
        "created",
        "modified",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["price", "is_available"]

admin.site.register(Product, ProductAdmin)