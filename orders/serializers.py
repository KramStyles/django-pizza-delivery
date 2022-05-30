from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=Order.SIZES)
    # order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'quantity', 'order_status']
        read_only_fields = ['order_status']


class OrderDetailSerializer(OrderSerializer):
    order_status = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    # OrderSerializer.Meta.fields.extend(['created_at', 'updated_at'])
    del OrderSerializer.Meta.fields
    OrderSerializer.Meta.exclude = ['customer']


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.ChoiceField(choices=Order.ORDER_STATUS)

    class Meta:
        model = Order
        fields = ['id', 'order_status', 'size']
        read_only_fields = ['size']
