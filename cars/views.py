from django.shortcuts import render
from users.permissions import CustomUserAccessPermission, UserInfoUpdatePermission
from .models import Cars
from .serializers import CarSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class CarListView(generics.ListCreateAPIView):

    queryset = Cars.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        print(Cars.objects.all())
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)
    
    def update(request, *args, **kwargs):
        print(request.data)



class CarDetailView(APIView):
    # permission_classes = [UserInfoUpdatePermission, CustomUserAccessPermission]

    def get(self, request, carId=None, *args, **kwargs):

        car = Cars.objects.get(id=carId)
        if not car:
            return Response(
                {"res": "Object with car id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = CarSerializer(car)    ### Loged in User Can see his more detailed Information : is_superuser, is_staff etc
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        car = Cars.objects.get(id=request.data.get(id))
        if not car:
            return Response(
                {"res": "Object with Car id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'id':request.data.get('id'),
            'name':request.data.get('name'),
            'description':request.data.get('description'),
            'buyingPrice': request.data.get('buyingPrice'),
            'sellingPrice': request.data.get('sellingPrice'),
            'createdAt': request.data.get('createdAt'),
            'ownerId': request.data.get('ownerId'),
            'carImg': request.data.get('createdAt')
        }

        serializer = CarSerializer(instance=Cars, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        succulent = Cars.objects.get(id=user_id)
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
