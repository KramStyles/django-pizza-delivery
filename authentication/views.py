from rest_framework import generics, response, status

from . import serializers


class CreateUserApiView(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_200_OK)
