from rest_framework import serializers
from .models import Category, Book, Review, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'bookcover', 'introduction']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname')
    book = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Review
        fields = '__all__'

class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='review_set')  # review_set을 통해 연결
    class Meta:
        model = Book
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname') 
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
