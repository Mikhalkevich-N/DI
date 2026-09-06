from django.http import HttpResponse
import json

# СЛОВАРЬ С РЕЦЕПТАМИ
data = {
    'omlet': {'яйца, шт': 2, 'молоко, л': 0.1, 'соль, ч.л.': 0.5},
    'pasta': {'макароны, г': 100, 'сыр, г': 50, 'вода, л': 2},
    'buter': {'хлеб, ломтик': 1, 'колбаса, ломтик': 2},
}


def create_recipe_response(request, recipe_key):
    recipe = dict(data.get(recipe_key, {}))
    
    servings = request.GET.get('servings')
    if servings is not None:
        try:
            servings = int(servings)
            recipe = {key: value * servings for key, value in recipe.items()}
        except ValueError:
            pass
    
    # Формируем текстовый вывод
    lines = [f"{key}: {value}" for key, value in recipe.items()]
    msg = "\n".join(lines)
    
    return HttpResponse(msg, content_type='text/plain; charset=utf-8')


def omlet_view(request):
    return create_recipe_response(request, 'omlet')


def pasta_view(request):
    return create_recipe_response(request, 'pasta')


def buter_view(request):
    return create_recipe_response(request, 'buter')