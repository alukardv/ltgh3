from django.core.management.base import BaseCommand

from app1.models import Region


class Command(BaseCommand):
    help = 'Імпорт міст з файлу'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Шлях до файлу для імпорту')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                region, idx = file.readline().rstrip(), 1

                while region:
                    Region.objects.create(title=region)
                    print(f'{idx:>4}. Успішно імпортовано [{region}]')

                    region = file.readline().rstrip()
                    idx += 1

        except FileNotFoundError:
            print(f'Файл {file_path} не знайдено')
