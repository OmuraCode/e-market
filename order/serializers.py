from rest_framework import serializers

from order.models import Order


class OrderUserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = '__all__'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     repr['total_sum'] =


