import pytest

from orders.models import Order


@pytest.mark.django_db
class TestOrderModel:
    def test_order_creation(self):
        order = Order.objects.create(
            table_number='10',
            status='pending',
            items={'Steak': 1200, 'Wine': 800}
        )
        assert order.table_number == '10'
        assert order.total_price == 2000
        assert str(order) == f'Заказ №{order.id} - Стол 10'
