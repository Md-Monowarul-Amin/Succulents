import datetime
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, first_name, last_name="", is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_staff = is_staff
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name=""):
        
        return self.create_user(email, password, first_name, last_name, True, True, True)