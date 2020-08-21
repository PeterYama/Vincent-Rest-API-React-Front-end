from django.urls import path
from .views import ListPost, PostDetail

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', ListPost.as_view())
]