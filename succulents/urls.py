# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import *
from .views import (
    SucculentListView,
    SucculentDetailView
)
urlpatterns = [
    path('SucculentList/', SucculentListView.as_view()),
    path('SucculentDetail/<int:succulent_id>/', SucculentDetailView.as_view()),
]
