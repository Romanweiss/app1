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
    '''для авто заполнения слага - URL'''
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    '''для авто заполнения слага - URL'''
    prepopulated_fields = {"slug": ("name",)}
