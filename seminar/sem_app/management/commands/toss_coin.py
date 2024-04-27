from django.core.management.base import BaseCommand
from sem_app.models import TossCoin


class Command(BaseCommand):
    help = 'Get user by id'

    # add_arguments позволяет парсить командную строку
    def handle(self, *args, **kwargs):
        toss = TossCoin()
        toss.save()
        self.stdout.write(f'{toss}')
