# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import *

urlpatterns = [
    path('SucculentList/', SucculentListView.as_view()),
    path('SucculentDetail/<pk>/', SucculentDetailView.as_view()),
]
