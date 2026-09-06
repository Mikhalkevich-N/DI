from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime('%H:%M:%S')
    # возвращается просто текст
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        files = os.listdir('.')                                                         
        msg = 'Список файлов в рабочей директории:<br>' + '<br>'.join(files)            
    except Exception as e:
        msg = f'Произошла ошибка: {str(e)}'                                             
    return HttpResponse(msg)