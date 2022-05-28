from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email is required!"))

        email = self.normalize_email(email)  # Changes the case of the domain part of the email
        new_user = self.model(email=email, **extra_fields)

        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_active', False)

        if not extra_fields.get('is_active'):
            raise ValueError(_("Superuser should be active"))
