# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from .views import *
from .views import (
    CarListView,
    CarDetailView
)
urlpatterns = [
    path('carList/', CarListView.as_view()),
    path('carDetail/<int:carId>/', CarDetailView.as_view()),
]
