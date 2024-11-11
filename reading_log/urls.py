from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import GuestViewSet, ReadingLogViewSet, FolderViewSet, BookSearchViewSet, UserReadingLogViewSet


router = DefaultRouter()
router.register(r'reading_logs', ReadingLogViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'user_reading_logs', UserReadingLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('guest/', GuestViewSet.as_view(), name='guest_view'),
    path('books/search/', BookSearchViewSet.as_view(), name='book_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)