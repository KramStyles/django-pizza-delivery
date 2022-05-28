from rest_framework import generics, response, status


class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return response.Response('Hello there', status=status.HTTP_200_OK)
