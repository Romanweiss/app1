from django.contrib import admin
from carts.admin import CartTabAdmin
from goods.models import Categories
from orders.admin import OrderTabulareAdmin

from users.models import User

#admin.site.register(User)

@admin.register(User)
class Usermin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email']
    search_fields = ['username','first_name', 'last_name', 'email']

    inlines = [CartTabAdmin, OrderTabulareAdmin]
