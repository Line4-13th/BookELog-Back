from django.urls import path
from .views import MyPageGuestViewSet, LoginViewSet, SignupViewSet

urlpatterns = [
    path('guest/', MyPageGuestViewSet.as_view(), name='mypage_guest'),
    path('login/', LoginViewSet.as_view(), name='login'),
    path('signup/', SignupViewSet.as_view(), name='signup'),
    
]