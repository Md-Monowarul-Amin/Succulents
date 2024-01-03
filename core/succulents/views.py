from django.shortcuts import render
from users.permissions import CustomUserAccessPermission, UserInfoUpdatePermission
from .models import Succulent
from .serializers import SucculentSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class SucculentListView(generics.ListCreateAPIView):

    queryset = Succulent.objects.all()
    serializer_class = SucculentSerializer

    def get(self, request, *args, **kwargs):
        print(Succulent.objects.all())
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)
    def update(request, *args, **kwargs):
        print(request.data)



class SucculentDetailView(APIView):
    # permission_classes = [UserInfoUpdatePermission, CustomUserAccessPermission]

    def get(self, request, succulent_id=None, *args, **kwargs):

        succulent = Succulent.objects.get(id=succulent_id)
        if not succulent:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = SucculentSerializer(succulent)    ### Loged in User Can see his more detailed Information : is_superuser, is_staff etc
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        succulent = Succulent.objects.get(id=request.user.id)
        if not succulent:
            return Response(
                {"res": "Object with succulent id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'id':request.data.get('id'),
            'name':request.data.get('name'),
            'succulent_type':request.data.get('succulent_type'),
            'importedFrom': request.data.get('importedFrom'),
            'buyingPrice': request.data.get('buyingPrice'),
            'sellingPrice': request.data.get('sellingPrice')
        }

        serializer = SucculentSerializer(instance=succulent, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        succulent = Succulent.objects.get(id=user_id)
        if not succulent:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        succulent.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
