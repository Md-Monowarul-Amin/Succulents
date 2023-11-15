from django.shortcuts import render
from .models import Succulent
from .serializers import SucculentSerializer
from rest_framework import generics

# Create your views here.

class SucculentListView(generics.ListCreateAPIView):
    queryset = Succulent.objects.all()
    serializer_class = SucculentSerializer

    # def get(self, request, *args, **kwargs):
    #     print(Succulent.objects.all())
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     return self.create(request, *args, **kwargs)


class SucculentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Succulent.objects.all()
    serializer_class = SucculentSerializer

