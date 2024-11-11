from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import MyPageGuestViewSet, LoginViewSet, SignupViewSet, MyPageViewSet, ReviewListViewSet, QuestionListViewSet


urlpatterns = [
    path('', MyPageViewSet.as_view(), name='mypage'),
    path('guest/', MyPageGuestViewSet.as_view(), name='mypage_guest'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('signup/', SignupViewSet.as_view(), name='signup'),
    path('reviews/', ReviewListViewSet.as_view(), name='review_list'),
    path('questions/', QuestionListViewSet.as_view(), name='question_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
