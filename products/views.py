from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializar_list import *

from .models import ProductPrice, ProductAttribute, Products


# product
class ProductListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()


# Product Attribute
class ProductAttributeListView(generics.ListCreateAPIView):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializar

    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        product = get_object_or_404(
            models.Products, pk=self.kwargs.get('pk')

        )
        serializer.save(product=product)


class ProductAttributeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductAttributeSerializar
    queryset = ProductAttribute.objects.all()

    def get_object(self):
        return self.queryset.get(id=self.kwargs.get('id'))


# ProductPrice
class ProductPriceListView(generics.ListCreateAPIView):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializar

    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs.get('pk'))


class ProductPriceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductPriceSerializar
    queryset = ProductPrice.objects.all()

    def get_object(self):
        return self.queryset.get(id=self.kwargs.get('id'))
