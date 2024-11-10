from rest_framework import serializers
from django.contrib.auth.models import User

class SignupSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        nickname = validated_data.pop('nickname')
        user = User.objects.create_user(**validated_data)
        user.userprofile.nickname = nickname
        user.userprofile.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()