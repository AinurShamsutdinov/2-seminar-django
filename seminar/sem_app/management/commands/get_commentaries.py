from django.core.management.base import BaseCommand
from sem_app.models import Commentary, Article, Author


class Command(BaseCommand):
    help = 'Get author commentaries'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('amount', type=int, help='Amount of commentaries')

    def handle(self, *args, **kwargs):
        author_name = kwargs.get('name')
        amount = kwargs.get('amount')
        authors = Author.objects.all().filter(name=author_name)[:amount]
        commentaries = list()
        for author in authors:
            author_comments = Commentary.objects.all().filter(author)
