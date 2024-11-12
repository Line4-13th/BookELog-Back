from django.urls import path
from .views import BookViewSet, BookDetailViewSet, QuestionViewSet

urlpatterns = [
    # BookViewSet 관련 엔드포인트
    path('', BookViewSet.as_view({'get': 'list'}), name='book-list'),
    path('bookdetail/', BookDetailViewSet.as_view({'get': 'list'}), name='book-detail-list'),
    path('bookdetail/<int:pk>/', BookDetailViewSet.as_view({'get': 'retrieve'}), name='book-detail'),

    # 명시적으로 BookDetailViewSet에서 review 추가 경로 설정
    path('bookdetail/<int:pk>/review/', BookDetailViewSet.as_view({'post': 'add_review'}), name='add-review'),
    # QuestionViewSet 관련 엔드포인트
    path('bookdetail/<int:book_id>/question/', QuestionViewSet.as_view({'post': 'add_question'}), name='add-question'),
    path('bookdetail/<int:book_id>/qna_list/', QuestionViewSet.as_view({'get': 'list_questions'}), name='qna-list'),
    path('bookdetail/<int:book_id>/<int:question_id>/answer/', QuestionViewSet.as_view({'post': 'add_answer'}), name='add-answer'),
    path('bookdetail/<int:book_id>/<int:question_id>/answers/', QuestionViewSet.as_view({'get': 'list_answers'}), name='list-answers'),
]
