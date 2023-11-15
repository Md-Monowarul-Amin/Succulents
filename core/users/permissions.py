from . models import CustomUser
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from django.contrib.auth.models import User, AbstractUser


class UserInfoUpdatePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id


class CustomUserAccessPermission(BasePermission):
    message = 'Accessing is restricted to Custom User Only'
        
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        # print( "is_custom", isinstance(obj, AbstractUser))

        #print( "is_custom", isinstance(obj, CustomUser))
        #return obj.id == request.user.id
        return isinstance(obj, CustomUser)
