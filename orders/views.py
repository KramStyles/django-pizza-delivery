from rest_framework import generics, response, status

from .serializers import OrderSerializer


class OrderListCreateApiView(generics.GenericAPIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
