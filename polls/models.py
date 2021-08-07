from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200, default='default name')

class Book(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateTimeField('date of publishing')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def is_valid(self):
        pass

