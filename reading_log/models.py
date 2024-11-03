from django.db import models
from books.models import Book

# Create your models here.

class ReadingLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()

class Folder(models.Model):
    name = models.CharField(max_length=100)
    reading_logs = models.ManyToManyField(ReadingLog, blank=True)