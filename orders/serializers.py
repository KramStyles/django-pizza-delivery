from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    size = serializers.ChoiceField(choices=Order.SIZES)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['size', 'quantity', 'order_status']
