# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db import transaction
# from django.forms import ValidationError
# from django.shortcuts import redirect, render

# from carts.models import Cart

# from orders.forms import CreateOrderForm
# from orders.models import Order, OrderItem


# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     user = request.user
#                     cart_items = Cart.objects.filter(user=user)

#                     if cart_items.exists():
#                         # Создать заказ
#                         order = Order.objects.create(
#                             user=user,
#                             phone_number=form.cleaned_data['phone_number'],
#                             requires_delivery=form.cleaned_data['requires_delivery'],
#                             delivery_address=form.cleaned_data['delivery_address'],
#                             payment_on_get=form.cleaned_data['payment_on_get'],
#                         )
#                         # Создать заказанные товары
#                         for cart_item in cart_items:
#                             product=cart_item.product
#                             name=cart_item.product.name
#                             price=cart_item.product.sell_price()
#                             quantity=cart_item.quantity


#                             if product.quantity < quantity:
#                                 raise ValidationError(f'Недостаточное количество товара {name} на складе\
#                                                        В наличии - {product.quantity}')

#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                             product.quantity -= quantity
#                             product.save()

#                         # Очистить корзину пользователя после создания заказа
#                         cart_items.delete()

#                         messages.success(request, 'Заказ оформлен!')
#                         return redirect('user:profile')
#             except ValidationError as e:
#                 messages.success(request, str(e))
#                 return redirect('cart:order')
#     else:
#         initial = {
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#             }

#         form = CreateOrderForm(initial=initial)

#     context = {
#         'title': 'Home - Оформление заказа',
#         'form': form,
#         'orders': True,
#     }
#     return render(request, 'orders/create_order.html', context=context)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from carts.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


class CreateOrderView(LoginRequiredMixin, CreateView):
    """
    В этом классе мы используем класс LoginRequiredMixin для проверки авторизации пользователя и класс CreateView для создания заказа.
    """

    template_name = "orders/create_order.html"
    form_class = CreateOrderForm

    def get_context_data(self, **kwargs):
        """
        Метод get_context_data() используется для добавления дополнительных данных в контекст шаблона. В этом методе мы переопределяем контекст, добавляя туда нужные нам данные.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Оформление заказа"
        context["orders"] = True
        return context

    def get_initial(self):
        """
        Метод get_initial() используется для установки начальных значений формы. В этом методе мы переопределяем начальные значения, добавляя туда имя и фамилию авторизованного пользователя.
        """
        initial = super().get_initial()
        initial["first_name"] = self.request.user.first_name
        initial["last_name"] = self.request.user.last_name
        return initial

    def form_valid(self, form):
        """
        Метод form_valid() используется для обработки данных формы после ее валидации. В этом методе мы переопределяем стандартную реализацию метода, добавляя туда логику создания заказа, создания заказанных товаров, проверки наличия товаров на складе и очистки корзины пользователя.
        """

        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    # Создать заказ
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data["phone_number"],
                        requires_delivery=form.cleaned_data["requires_delivery"],
                        delivery_address=form.cleaned_data["delivery_address"],
                        payment_on_get=form.cleaned_data["payment_on_get"],
                    )
                    # Создать заказанные товары
                    for cart_item in cart_items:
                        product = cart_item.product
                        name = cart_item.product.name
                        price = cart_item.product.sell_price()
                        quantity = cart_item.quantity

                        if product.quantity < quantity:
                            raise ValidationError(
                                f"Недостаточное количество товара {name} на складе\
                                                   В наличии - {product.quantity}"
                            )

                        OrderItem.objects.create(
                            order=order,
                            product=product,
                            name=name,
                            price=price,
                            quantity=quantity,
                        )
                        product.quantity -= quantity
                        product.save()

                    # Очистить корзину пользователя после создания заказа
                    cart_items.delete()

                    messages.success(self.request, "Заказ оформлен!")
                    return redirect("user:profile")
        except ValidationError as e:
            messages.success(self.request, str(e))
            return redirect("cart:order")
