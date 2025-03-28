import json

import pytest
from django.urls import reverse

from orders.models import Order


@pytest.mark.django_db
class TestOrderViews:
    def test_order_create_get(self, client):
        url = reverse('order_create')
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context

    def test_order_create_post_valid(self, client):
        url = reverse('order_create')
        data = {
            'table_number': '5',
            'status': 'pending',
            'items_json': json.dumps(
                {'Burger': 500, 'Fries': 200}),
        }
        response = client.post(url, data, follow=True)

        assert response.status_code in [200, 302]
        assert Order.objects.count() == 1
        assert Order.objects.first().table_number == 5

    def test_order_list_with_filter(self, client):
        Order.objects.create(
            table_number='1',
            items={'Burger': 500}, status='pending')
        Order.objects.create(
            table_number='2',
            items={'Pizza': 700}, status='paid')

        response = client.get(
            reverse('order_list') + '?table_number=1'
        )
        assert response.status_code == 200
        assert len(response.context['orders']) == 1

    def test_order_update_get(self, client):
        order = Order.objects.create(
            table_number='3',
            items={'Salad': 300}
        )
        url = reverse('order_update', args=[order.id])
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context

    def test_order_update_post(self, client):
        order = Order.objects.create(
            table_number='4',
            items={'Soup': 250},
            status='pending'
        )
        url = reverse('order_update', args=[order.id])
        data = {
            'table_number': '4',
            'status': 'ready',
            'items_json': json.dumps(
                {'Soup': 250, 'Bread': 50}
            ),
        }
        response = client.post(url, data)
        assert response.status_code == 302
        order.refresh_from_db()
        assert order.status == 'ready'
        assert 'Bread' in order.items

    def test_order_delete(self, client):
        order = Order.objects.create(
            table_number='5',
            items={'Coffee': 150}, status='pending'
        )
        url = reverse('order_delete', args=[order.id])
        response = client.post(url)
        assert response.status_code == 302
        assert Order.objects.count() == 0
