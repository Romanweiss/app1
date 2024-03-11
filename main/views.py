from django.http import HttpResponse
from django.shortcuts import render

# Функции в данном файле - views.py называются представлениями или контроллерами

# В параметр request попадает экземпляр класса HttpRequest,
# который содержит в себе все данные о запросе (статус пользователя, куки, метод запроса  GET, POST итд).


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse("About Page")
