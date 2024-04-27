import datetime
import random

from django.db import models

# Create your models here.


class TossCoin(models.Model):
    result = models.CharField(max_length=100)
    date = models.DateField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        rand = random.randrange(0, 2)
        if rand == 0:
            self.result = 'Head'
        else:
            self.result = 'Tail'
        self.date = datetime.datetime.now()

    def __str__(self):
        return f'Result: {self.result}, Date: {self.date}'
