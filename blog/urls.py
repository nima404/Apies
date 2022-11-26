from django.urls import path
from .views import ArticleView, CommentView, like_comment_view, dislike_comment_view

from .routers import router

app_name = 'blog'

urlpatterns = [
    path('article/<int:pk>/<str:slug>/', ArticleView.as_view({'get': 'retrieve'}), name="article_detail"),
    path('article/', ArticleView.as_view({'get': 'list'})),
    path('comment/', CommentView.as_view()),
    path('comment/like/<int:pk>/', like_comment_view),
    path('comment/dislike/<int:pk>/', dislike_comment_view)
] + router.urls
