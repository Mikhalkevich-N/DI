import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            # Используем get_or_create, чтобы не создавать дубликаты,
            # если скрипт запускается повторно.
            Phone.objects.get_or_create(
                id=phone['id'],  # id - основной ключ
                defaults={
                    'name': phone['name'],
                    'price': phone['price'],
                    'image': phone['image'],
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'].lower() == 'true',  # Преобразуем "True"/"False" в bool
                    'slug': slugify(phone['name'])  # Генерируем слагифицированное название
                }
            )