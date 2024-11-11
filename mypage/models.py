from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypage_reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='mypage_reviews')
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypage_questions')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='mypage_questions')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Question by {self.user.username} on {self.book.title}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='mypage_answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypage_answers')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer by {self.user.username} for question {self.question.id}'