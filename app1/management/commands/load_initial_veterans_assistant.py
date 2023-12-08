import csv

from django.core.management.base import BaseCommand

from app1.models import VeteransAssistant, Region, TypeOfUser


class Command(BaseCommand):
    help = 'Load data from CSV into Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                region_id = row['region'].strip()
                region = Region.objects.get(id=region_id)

                type_of_user_id = row['type_of_user'].strip()
                type_of_user = TypeOfUser.objects.get(id=type_of_user_id)

                VeteransAssistant.objects.create(
                    surname=row['surname'].strip(),
                    name=row['name'].strip(),
                    patronymic=row['patronymic'].strip(),
                    phone_number=row['phone_number'].strip(),
                    date_of_birth=row['date_of_birth'].strip(),
                    time_create=row['time_create'].strip(),
                    time_update=row['time_update'].strip(),
                    region=region,
                    type_of_user=type_of_user,
                )
                print(f'Успішно імпортовано')
