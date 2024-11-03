from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category'),
    path('<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:book_id>/review/', views.BookReviewView.as_view(), name='book_review'),
    path('<int:book_id>/rate/', views.BookRateView.as_view(), name='book_rate'),
    path('<int:book_id>/question/', views.BookQuestionView.as_view(), name='book_question'),
    path('<int:book_id>/answer/', views.BookAnswerView.as_view(), name='book_answer'),
]