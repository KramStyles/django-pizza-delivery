from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

# from .models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=100)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=4)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        is_user = User.objects.filter(username = attrs['username']).exists()
        is_email = User.objects.filter(email = attrs['email']).exists()
        is_phone = User.objects.filter(phone_number = attrs['phone_number']).exists()

        if is_user: raise serializers.ValidationError(detail="User already exists")
        if is_email: raise serializers.ValidationError(detail="Email already exists")
        if is_phone: raise serializers.ValidationError(detail='Phone already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])

        # new_user.save()
        return new_user
