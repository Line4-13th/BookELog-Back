from rest_framework import serializers
from .models import ReadingLog, Folder

class ReadingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingLog
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'
