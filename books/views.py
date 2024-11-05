from django.shortcuts import render
from rest_framework import viewsets, mixins
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Category, Book, Review, Question, Answer
from .serializers import BookDetailSerializer, BookSerializer, ReviewSerializer, QuestionSerializer, AnswerSerializer

# Create your views here.

class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        search = self.request.query_params.get('search')

        if category:
            queryset = queryset.filter(category__name=category)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(category__name__icontains=search)
            )
        return queryset

class BookDetailViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

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
