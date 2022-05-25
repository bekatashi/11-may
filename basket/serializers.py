from rest_framework import serializers
from product.models import Product
from basket.models import Order





class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()
    def validate(self, attrs):
        data = {}
        print(attrs)
        try:
            product = Product.objects.get(pk=attrs['product'])
        except Product.DoesNotExists:
            raise serializers.ValidationError('Product not found')
        count = attrs['quantity']
        data['count'] = count
        data['product'] = product.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Order.objects.create(product=product, user=user, quantity=data['count'])
