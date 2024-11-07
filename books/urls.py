from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookDetailViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')
router.register(r'bookdetail', BookDetailViewSet, basename='book-detail')
router.register(r'bookdetail/(?P<book_id>\d+)/qna', QuestionViewSet, basename='book-qna')

urlpatterns = [
    path('', include(router.urls)),
]