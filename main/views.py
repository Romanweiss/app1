from django.http import HttpResponse
from django.shortcuts import render

# Функции в данном файле - views.py называются представлениями или контроллерами

# В параметр request попадает экземпляр класса HttpRequest,
# который содержит в себе все данные о запросе (статус пользователя, куки, метод запроса  GET, POST итд).


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
        
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Какой то пространный текст о том, что наш магазин - самый лучший'
        
    }
    return render(request, 'main/about.html', context)
