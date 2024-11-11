from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny  # 나중에 IsAuthenticated로 변경 가능
from .models import ReadingLog, Folder, UserReadingLog
from books.models import Book
from .serializers import ReadingLogSerializer, FolderSerializer, BookSerializer, UserReadingLogSerializer, UserReadingLogPreviewSerializer
from rest_framework.decorators import action


class GuestViewSet(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "로그인 후, 해당 서비스를 이용해 주세요.",
            "actions": {
                "login": "로그인 페이지로 이동",
                "signup": "회원가입 페이지로 이동"
            }
        })

class ReadingLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReadingLog.objects.all()
    serializer_class = ReadingLogSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def dots(self, request):
        month = request.query_params.get('month')
        logs = ReadingLog.objects.filter(date__startswith=month)
        dates = logs.values_list('date', flat=True)
        return Response({"dots": dates})

class FolderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def create_folder(self, request):
        name = request.data.get('name', '새 파일')
        folder = Folder.objects.create(name=name)
        serializer = self.get_serializer(folder)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookSearchViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

class UserReadingLogViewSet(viewsets.ModelViewSet):
    queryset = UserReadingLog.objects.all()
    serializer_class = UserReadingLogSerializer

    @action(detail=False, methods=['get'], url_path='folder/(?P<folder_id>[^/.]+)')
    def list_by_folder(self, request, folder_id=None):
        reading_logs = UserReadingLog.objects.filter(folder_id=folder_id)
        serializer = UserReadingLogPreviewSerializer(reading_logs, many=True)
        return Response(serializer.data)