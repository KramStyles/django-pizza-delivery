from rest_framework import generics, response, status

from . import serializers


class CreateUserApiView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def get(self, request):
        return response.Response('Hello there', status=status.HTTP_200_OK)
