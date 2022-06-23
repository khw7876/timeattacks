from dataclasses import fields
from rest_framework import serializers

from .models import Category as CategoryModel
from .models import Item as ItemModel
from .models import Order as OrderModel
from .models import ItemOrder as ItemOrderModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        Model = CategoryModel
        fields = ["name"]

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        Model = ItemModel
        fields = ["name", "category", "image_url"]

class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        Model = OrderModel
        fields = ["delivery_address", "order_date", "item"]

class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    class Meta:
        Model = OrderModel
        fields = ["order", "item", "item_count"]