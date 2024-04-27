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


class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __init__(self, name, last_name, email, biography, birthday, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.last_name = last_name
        self.full_name = f'{name} {last_name}'
        self.email = email
        self.biography = biography
        self.birthday = birthday


class Article(models.Model):
    head = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)
