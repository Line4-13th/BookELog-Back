from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.utils import timezone

# Create your models here.

class ReadingLog(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Reading log on {self.date}"
    

class Folder(models.Model):
    name = models.CharField(max_length=100)
    reading_logs = models.ManyToManyField(ReadingLog, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    
class UserReadingLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # 선택한 책
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, blank=True, null=True)  # 폴더 선택
    rating = models.IntegerField(default=0)  # 별점 (0~5점)
    start_date = models.DateField(blank=True, null=True)  # 읽기 시작 날짜
    completion_date = models.DateField(blank=True, null=True)  # 완독 날짜
    notes = models.TextField(blank=True, null=True)  # 메모
    image = models.ImageField(upload_to='reading_log_images/', blank=True, null=True)  # 이미지 첨부
    created_at = models.DateTimeField(default=timezone.now)  # 생성 날짜

    def __str__(self):
        return f"{self.book.title} - {self.folder.name if self.folder else 'No Folder'}"