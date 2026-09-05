from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True, required=False)

    class Meta:
        model = Stock
        fields = ['id', 'name', 'address', 'positions']

    def create(self, validated_data):
        # Достаем позиции (если они есть), иначе пустой список
        positions = validated_data.pop('positions', [])

        # Создаем склад
        stock = super().create(validated_data)

        # Создаем позиции на складе
        for position_data in positions:
            StockProduct.objects.create(stock=stock, **position_data)

        return stock

    def update(self, instance, validated_data):
        # Достаем позиции (если они есть)
        positions = validated_data.pop('positions', None)

        # Обновляем склад
        stock = super().update(instance, validated_data)

        # Обновляем или создаем позиции
        if positions is not None:
            for position_data in positions:
                StockProduct.objects.update_or_create(
                    stock=stock,
                    product=position_data['product'],
                    defaults={
                        'quantity': position_data.get('quantity', 1),
                        'price': position_data.get('price', 0),
                    }
                )

        return stock