# todo/todo_api/urls.py : API urls.py
from django.urls import path, include

from .views import (
    CustomerUserListView,
    RegisterUserView,
    CustomUserDetailView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('detail/', CustomerUserListView.as_view()),
    path('detail/<int:user_id>', CustomUserDetailView.as_view()),
]