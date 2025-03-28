import json

from django.db import models


class Order(models.Model):
    STATUS_CHOICE = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]
    table_number = models.PositiveIntegerField(verbose_name="Номер стола")
    items = models.JSONField()
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICE,
        default='pending',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    def calculate_total_price(self) -> None:
        if isinstance(self.items, str):
            self.items = json.loads(self.items)
        self.total_price = sum(int(price) for price in self.items.values())

    def save(self, *args, **kwargs) -> None:
        self.calculate_total_price()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Заказ №{self.id} - Стол {self.table_number}"
