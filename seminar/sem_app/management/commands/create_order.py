import datetime

from django.core.management.base import BaseCommand
from sem_app.models import Order, Client, Item


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('client_name', type=str, help='Name of client')
        parser.add_argument('item_name', type=str, help='Name of item')
        
    def handle(self, *args, **kwargs):
        client_order = Client.objects.get(name=kwargs.get('client_name'))
        item = Item.objects.get(name=kwargs.get('item_name'))
        order = Order(client=client_order, full_price=item.price, date_order=datetime.datetime.now())
        order.save()
        order.items.set(list())
        order.items.add(item)
        order.save()
