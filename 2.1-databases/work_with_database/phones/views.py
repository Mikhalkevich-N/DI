from django.shortcuts import render, get_object_or_404
from .models import Phone


def index(request):
    return render(request, 'index.html')


def show_catalog(request):
    # Получаем параметр сортировки из запроса (например, ?sort=name)
    sort_param = request.GET.get('sort')
    
    # Базовый запрос ко всем телефонам
    phones = Phone.objects.all()
    
    # Применяем сортировку в зависимости от параметра
    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')
        
    # Передаем телефоны в шаблон
    context = {
        'phones': phones
    }
    return render(request, 'catalog.html', context)


def show_product(request, slug):
    # Ищем конкретный телефон по слагу (например, 'iphone-x')
    phone = get_object_or_404(Phone, slug=slug)
    
    context = {
        'phone': phone
    }
    return render(request, 'product.html', context)