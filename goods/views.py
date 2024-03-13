from django.shortcuts import render

# импорт модели для дальнейшей работы с ней
from goods.models import Products


def catalog(request):

    # получаем информацию из бд в отдельный файл
    goods = Products.objects.all()

    context = {
        "title": "Home - каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
