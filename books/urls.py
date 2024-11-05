from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookDetailViewSet

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')
router.register(r'bookdetail', BookDetailViewSet, basename='book-detail')


urlpatterns = [
    path('', include(router.urls)),
]