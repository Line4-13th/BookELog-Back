from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
]