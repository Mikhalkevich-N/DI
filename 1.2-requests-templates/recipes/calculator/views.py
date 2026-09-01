from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def omlet_view(request):
    # Получаем базовый рецепт омлета из глобальных данных
    recipe = dict(data.get('omlet', {}))
    
    # Обрабатываем необязательный параметр servings
    servings = request.GET.get('servings')
    if servings is not None:
        # Преобразуем строку в число и умножаем ингредиенты
        try:
            servings = int(servings)
            recipe = {key: value * servings for key, value in recipe.items()}
        except ValueError:
            # Если ввели не число, оставляем как есть (1 порция)
            pass
    
    # Формируем контекст как в примере
    context = {
        'recipe': recipe
    }
    
    # Рендерим шаблон (предполагается, что шаблон называется omlet.html)
    return render(request, 'calculator/omlet.html', context)


def pasta_view(request):
    recipe = dict(data.get('pasta', {}))
    
    servings = request.GET.get('servings')
    if servings is not None:
        try:
            servings = int(servings)
            recipe = {key: value * servings for key, value in recipe.items()}
        except ValueError:
            pass
    
    context = {
        'recipe': recipe
    }
    
    return render(request, 'calculator/pasta.html', context)


def buter_view(request):
    recipe = dict(data.get('buter', {}))
    
    servings = request.GET.get('servings')
    if servings is not None:
        try:
            servings = int(servings)
            recipe = {key: value * servings for key, value in recipe.items()}
        except ValueError:
            pass
    
    context = {
        'recipe': recipe
    }
    
    return render(request, 'calculator/buter.html', context)