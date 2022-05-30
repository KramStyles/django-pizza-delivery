from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status

from . import serializers
from .models import Order


# class OrderListCreateApiView(generics.ListCreateAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()

class OrderListCreateAPIView(generics.GenericAPIView):
    serializer_class = serializers.OrderSerializer
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
    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(data=request.data, instance=order)

        if serializer.is_valid():
            serializer.save()

            return response.Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        order.delete()

        return response.Response(data='Deleted', status=status.HTTP_204_NO_CONTENT)


class OrderStatusUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    queryset = Order.objects.all()

    # def get(self, request, pk):
    #     order = get_object_or_404(Order, pk=pk)
    #     serializer = self.serializer_class(instance=order)
    #     return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrderView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    queryset = Order.objects.all()

    def get(self, request, user_id):
        orders = Order.objects.filter(customer_id=user_id)
        serializer = self.serializer_class(instance=orders, many=True)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
