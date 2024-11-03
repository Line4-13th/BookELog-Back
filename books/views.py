from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Book, Review, Question, Answer
from .serializers import CategorySerializer, BookSerializer, ReviewSerializer, QuestionSerializer, AnswerSerializer

# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class BookDetailView(APIView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookReviewView(APIView):
    def post(self, request, book_id):
        # 리뷰 작성 로직 구현
        pass

class BookRateView(APIView):
    def post(self, request, book_id):
        # 평점 주기 로직 구현
        pass

class BookQuestionView(APIView):
    def post(self, request, book_id):
        # 질문 작성 로직 구현
        pass

class BookAnswerView(APIView):
    def post(self, request, book_id):
        # 답변 작성 로직 구현
        pass
