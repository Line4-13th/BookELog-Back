from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from .models import Review, Question
from reading_log.models import UserReadingLog
from .serializers import SignupSerializer, LoginSerializer, ReviewPreviewSerializer, QuestionPreviewSerializer, MyPageSerializer, ReadingLogCountSerializer
from datetime import timedelta
from django.utils import timezone


# Create your views here.

class MyPageGuestViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({
            "message": "로그인하고 다양한 서비스를 경험해보세요.",
            "actions": {
                "login": "로그인 페이지로 이동",
                "signup": "회원가입 페이지로 이동"
            }
        })

class SignupViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            if username is None or password is None:
                return Response({"message": "username과 password를 모두 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)
            return Response({"message": "잘못된 회원 정보"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyPageViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user = request.user
        now = timezone.now()

        # 독서기록장 개수 통계 (1일, 1개월, 1년)
        day_count = UserReadingLog.objects.filter(user=user, created_at__gte=now - timedelta(days=1)).count()
        month_count = UserReadingLog.objects.filter(user=user, created_at__gte=now - timedelta(days=30)).count()
        year_count = UserReadingLog.objects.filter(user=user, created_at__gte=now - timedelta(days=365)).count()

        # 최신 리뷰 1개 가져오기
        latest_review = Review.objects.filter(user=user).order_by('-created_at').first()

        # 최신 질문(Q&A) 1개 가져오기
        latest_question = Question.objects.filter(user=user).order_by('-created_at').first()

        # 마이페이지 데이터 생성
        mypage_data = {
            'user': user,
            'reading_log_count': {
                'day_count': day_count,
                'month_count': month_count,
                'year_count': year_count,
            },
            'latest_review': latest_review,
            'latest_question': latest_question,
        }

        serializer = MyPageSerializer(mypage_data)
        return Response(serializer.data)
    

class ReviewListViewSet(generics.ListAPIView):
    serializer_class = ReviewPreviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-created_at')


class QuestionListViewSet(generics.ListAPIView):
    serializer_class = QuestionPreviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Question.objects.filter(user=self.request.user).order_by('-created_at')