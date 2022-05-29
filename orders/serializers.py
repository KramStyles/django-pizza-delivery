from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(max_length=20, default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'quantity', 'order_status']
