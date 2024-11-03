from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.ReadingLogCalendarView.as_view(), name='calendar'),
    path('folders/create/', views.FolderCreateView.as_view(), name='folder_create'),
]
