from atexit import register
from django.contrib import admin

from goods.models import Categories, Products

# Register your models here.
# регистрация таблиц для отображения в админке

# admin.site.register(Categories)

# admin.site.register(Products)


# тонкая настройка отображения в админке
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """для авто заполнения слага - URL"""

    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', ]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """для авто заполнения слага - URL"""

    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = [
        "discount",
    ]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]
