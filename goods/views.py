from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

# импорт модели для дальнейшей работы с ней
from goods.models import Products


def catalog(request, category_slug, page=1):

    if category_slug == 'all':
        # получаем информацию из бд в отдельный файл
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    # создаём пагинацию
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Home - каталог",
        "goods": current_page,
        'slug_url': category_slug
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)
