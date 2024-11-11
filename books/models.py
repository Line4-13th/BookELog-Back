from django.db import models
from mypage.models import UserProfile

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)
    bookcover = models.ImageField(null=True)
    publisher = models.CharField(max_length=255, null=True)
    date = models.DateField(null=True)
    link = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    introduction = models.TextField(null=True)
    star = models.IntegerField(null=True)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField()

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    content = models.TextField()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
