from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=100)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=4)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
