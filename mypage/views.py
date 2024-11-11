from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from .models import UserProfile
from .serializers import SignupSerializer, LoginSerializer

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
            return Response({"message": "잘못된 자격 증명"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
