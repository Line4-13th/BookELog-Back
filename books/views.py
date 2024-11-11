from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, generics, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth.models import User
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

class BookDetailViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    @action(detail=True, methods=['post'], url_path='review', permission_classes=[AllowAny])
    def add_review(self, request, pk=None):
        book = self.get_object()
        username = request.data.get('username')
        content = request.data.get('content')
        rating = request.data.get('rating')

        user = get_object_or_404(User, username=username)
        review = Review.objects.create(user=user, book=book, content=content, rating=rating)
        
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
    permission_classes = [AllowAny]

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Question.objects.filter(book__id=book_id)

    @action(detail=False, methods=['post'], url_path='question')
    def add_question(self, request, book_id=None):
        """특정 책에 질문을 추가하는 POST 요청 처리"""
        book = get_object_or_404(Book, id=book_id)
        content = request.data.get('content')
        username = request.data.get('username')

        user = get_object_or_404(User, username=username)
        
        question = Question.objects.create(book=book, user=user, content=content)
        q_serializer = self.get_serializer(question)
        return Response(q_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='qna_list')
    def list_questions(self, request, book_id=None):
        #모든 question들 반환
        questions = self.get_queryset()
        q_serializer = QuestionSerializer(questions, many=True)
        return Response(q_serializer.data)
    
    @action(detail=True, methods=['post'], url_path=r'(?P<question_id>\d+)/answer')
    def add_answer(self, request, pk=None, book_id=None, question_id=None):
        """특정 질문에 답변을 추가하는 POST 요청 처리"""
        question = get_object_or_404(Question, id=question_id, book_id=book_id)
        content = request.data.get('content')
        username = request.data.get('username')

        user = get_object_or_404(User, username=username)
        answer = Answer.objects.create(question=question, user=user, content=content)
        
        a_serializer = AnswerSerializer(answer)
        return Response(a_serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'], url_path='answers')
    def list_answers(self, request, book_id=None, pk=None):
        """특정 질문에 대한 모든 답변을 반환하는 GET 요청 처리"""
        question = get_object_or_404(Question, id=pk, book_id=book_id)
        question_data = QuestionSerializer(question).data

        answers = Answer.objects.filter(question=question)
        answers_data = AnswerSerializer(answers, many=True).data
        
        return Response({
            "question": question_data,
            "answers": answers_data
        })
