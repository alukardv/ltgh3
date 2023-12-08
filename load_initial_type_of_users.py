import csv

from django.core.management.base import BaseCommand

from app1.models import TypeOfUser


class Command(BaseCommand):
    help = 'Load data from CSV into Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                TypeOfUser.objects.create(
                    title=row['title'].strip(),

                )
                print(f'Успішно імпортовано')
