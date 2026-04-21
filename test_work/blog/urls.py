from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
    path('posts/<int:pk>/', views.PostDetailAPIView.as_view()),
    path('posts/<int:post_id>/comments/', views.CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailAPIView.as_view()),
]