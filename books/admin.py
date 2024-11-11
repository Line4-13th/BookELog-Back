from django.contrib import admin
from .models import Book, Category, Review, Question, Answer

# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Answer)

# admin ID : bookelog
# admin PassWord : qordpsem djemals (백엔드 어드민)