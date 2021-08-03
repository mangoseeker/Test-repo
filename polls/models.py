from django.db import models
import datetime
from django.utils import timezone



class Book(models.Model):
    name = models.CharField(max_length=200)
    year = models.DateTimeField('date of publishing')

class Author(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


