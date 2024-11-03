from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Review
from .serializers import UserProfileSerializer, ReviewSerializer

# Create your views here.

class UserProfileView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

class ReviewListView(APIView):
    def get(self, request):
        reviews = Review.objects.filter(user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
