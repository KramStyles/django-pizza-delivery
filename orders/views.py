from rest_framework import generics, response, status

from .serializers import OrderSerializer
from .models import Order


class OrderListCreateApiView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.GenericAPIView):
    def get(self, request, order_id):
        pass

    def post(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
