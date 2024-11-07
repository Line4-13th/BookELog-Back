from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Category, Book, Review, Question, Answer
from mypage.models import UserProfile
from .serializers import BookDetailSerializer, BookSerializer, ReviewSerializer, QuestionSerializer, AnswerSerializer
from django.shortcuts import get_object_or_404

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

class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    @action(detail=True, methods=['post'], url_path='review', permission_classes=[IsAuthenticated])
    def add_review(self, request, pk=None):
        book = self.get_object()
        username = request.data.get('username')
        content = request.data.get('content')
        rating = request.data.get('rating')

        user_profile = get_object_or_404(UserProfile, user__username=username)
        review = Review.objects.create(user=user_profile, book=book, content=content, rating=rating)
        
        review_serializer = ReviewSerializer(review)
        return Response(review_serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        book = self.get_object()
        book_serializer = self.get_serializer(book)

        reviews = Review.objects.filter(book=book)
        review_serializer = ReviewSerializer(reviews, many=True)

        data = book_serializer.data
        data['reviews'] = review_serializer.data
        return Response(data)
  

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Question.objects.filter(book__id=book_id)

    @action(detail=True, methods=['post'], url_path='question')
    def add_question(self, request, book_id=None):
        """특정 책에 질문을 추가하는 POST 요청 처리"""
        book = get_object_or_404(Book, id=book_id)
        content = request.data.get('content')
        username = request.data.get('username')

        user_profile = get_object_or_404(UserProfile, user__username=username)
        
        question = Question.objects.create(book=book, user=user_profile, content=content)
        serializer = self.get_serializer(question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='qna_list')
    def list_questions(self, request, book_id=None):
        #모든 question들 반환
        questions = self.get_queryset()
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)
    

class BookAnswerView(APIView):
    def post(self, request, book_id):
        # 답변 작성 로직 구현
        pass
