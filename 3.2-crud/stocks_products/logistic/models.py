from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Связь многие ко многим через промежуточную модель
    stocks = models.ManyToManyField(
        'Stock',
        through='StockProduct',
        related_name='products',
    )


class Stock(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class StockProduct(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='positions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    # Количество товара на складе
    quantity = models.PositiveIntegerField(default=1)
    # Цена за одну единицу товара на этом складе
    price = models.DecimalField(max_digits=12, decimal_places=2)