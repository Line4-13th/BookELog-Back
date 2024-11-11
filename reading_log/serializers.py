from rest_framework import serializers
from .models import ReadingLog, Folder, Book, UserReadingLog

class ReadingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingLog
        fields = ['date']

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'name', 'created_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover_image']


class UserReadingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReadingLog
        fields = [
            'id', 'book', 'folder', 'rating', 'start_date',
            'completion_date', 'notes', 'image', 'created_at'
        ]


class UserReadingLogPreviewSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title')

    class Meta:
        model = UserReadingLog
        fields = ['id', 'book_title', 'image']