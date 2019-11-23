from rest_framework import serializers
from . import models


class ProductPriceSerializar(serializers.ModelSerializer):
    class Meta:
        model = models.ProductPrice
        fields = (
            'id',
            'product',
            'product_attribute',
            'product_price'
        )


class ProductAttributeSerializar(serializers.ModelSerializer):

    class Meta:
        model = models.ProductAttribute
        fields = (
            'id',
            'product',
            'product_color',
            'product_size'
        )


class ProductSerializer(serializers.ModelSerializer):
    product = ProductPriceSerializar(many=True, read_only=True)

    class Meta:
        model = models.Products
        fields = (
            'id',
            'product_name',
            'product_code',
            'product_slug',
            'product'
        )

        def create(self, validated_data):
            return models.Products(**validated_data)

        def update(self, instance, validated_data):
            instance.id = validated_data.get('product_name', instance.id)
            instance.product_name = validated_data.get('product_name', instance.product_name)
            instance.product_code = validated_data.get('product_name', instance.product_code)
            instance.product_slug = validated_data.get('product_name', instance.product_slug)
            if instance is not None:
                return instance
            else:
                raise serializers.ValidationError('Must Fillup all ')


