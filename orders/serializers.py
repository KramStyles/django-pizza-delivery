from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=Order.SIZES)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'quantity', 'order_status']


class OrderDetailSerializer(OrderSerializer):
    order_status = serializers.CharField(max_length=20)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    # OrderSerializer.Meta.fields.extend(['created_at', 'updated_at'])
    OrderSerializer.Meta.fields = '__all__'
