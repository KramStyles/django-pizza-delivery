from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status

from .serializers import OrderSerializer, OrderDetailSerializer
from .models import Order


# class OrderListCreateApiView(generics.ListCreateAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()

class OrderListCreateAPIView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(customer=request.user)

            return response.Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
