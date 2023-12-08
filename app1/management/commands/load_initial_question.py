import csv

from django.core.management.base import BaseCommand

from app1.models import Question, UserTG, VeteransAssistant


class Command(BaseCommand):
    help = 'Load data from CSV into Django model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                user_gt_id = row['user_gt'].strip()
                user_gt = UserTG.objects.get(id=user_gt_id)

                veterans_assistant_id = row['veterans_assistant'].strip()
                veterans_assistant = VeteransAssistant.objects.get(id=veterans_assistant_id)

                Question.objects.create(
                    time_create=row['time_create'].strip(),
                    time_update=row['time_update'].strip(),
                    veterans_assistant=veterans_assistant,
                    user_gt=user_gt,
                    text_question=row['text_question'].strip(),
                )
                print(f'Успішно імпортовано')
