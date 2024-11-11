from django.contrib.auth.models import User
from rest_framework import serializers
from books.models import Review, Question, Answer
from reading_log.models import ReadingLog
from datetime import timedelta
from django.utils import timezone


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}  # 필요한 경우 email을 필수로 설정
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],  # 아이디
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name']  # 실제 유저 이름
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ReviewPreviewSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Review
        fields = ['id', 'book_title', 'content', 'rating', 'created_at']



class AnswerPreviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Answer
        fields = ['content', 'created_at', 'user']


class QuestionPreviewSerializer(serializers.ModelSerializer):
    answers = AnswerPreviewSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['content', 'answers', 'created_at']


class ReadingLogCountSerializer(serializers.Serializer):
    day_count = serializers.IntegerField()
    month_count = serializers.IntegerField()
    year_count = serializers.IntegerField()


class MyPageSerializer(serializers.Serializer):
    username = serializers.CharField(source='user.username')
    reading_log_count = ReadingLogCountSerializer()
    latest_review = ReviewPreviewSerializer()
    latest_question = QuestionPreviewSerializer()