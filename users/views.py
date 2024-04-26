import statistics
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, OwnUserSerializer
from .managers import CustomUserManager
from rest_framework import permissions
from .permissions import UserInfoUpdatePermission, CustomUserAccessPermission
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated, SAFE_METHODS, IsAdminUser

# Create your views here.
class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):

        data = {
            'email' : request.data.get('email'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'password' : request.data.get('password'),
        }
        
        print(data)
        serializer = UserSerializer(data=data)
        user = CustomUser.objects.create_user(data['email'], data['password'], data['first_name'], data['last_name'])
        user.save()
        #serializer.create_user(self, data, request.password)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerUserListView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        user = CustomUser.objects.all()
        if not user:
            return Response(
            {"res": "No CustomUser Object exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomUserDetailView(APIView):

    permission_classes = [UserInfoUpdatePermission, CustomUserAccessPermission]

    def get(self, request, user_id=None, *args, **kwargs):

        user = CustomUser.objects.get(id=user_id)
        if not user:
            return Response(
                {"res": "Object with user id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.user.id == user_id:          
            serializer = OwnUserSerializer(user)    ### Loged in User Can see his more detailed Information : is_superuser, is_staff etc
        else:
            serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, *args, **kwargs):
        user = CustomUser.objects.get(id=request.user.id)
        if not user:
            return Response(
                {"res": "Object with user id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'email': request.data.get('email'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'is_active': request.data.get('is_active')
        }

        serializer = UserSerializer(instance=user, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        if not user:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
