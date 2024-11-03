from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ReadingLog, Folder
from .serializers import ReadingLogSerializer, FolderSerializer

# Create your views here.

class ReadingLogCalendarView(APIView):
    def get(self, request):
        # 달력에 표시할 독서 기록 조회 로직
        pass

class FolderCreateView(APIView):
    def post(self, request):
        # 폴더 생성 로직
        pass