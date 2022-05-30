from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, response, status

from . import serializers


class CreateUserApiView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(operation_summary="Api to create user account")
    def post(self, request):
        """
        API used to create a new account.
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_200_OK)
