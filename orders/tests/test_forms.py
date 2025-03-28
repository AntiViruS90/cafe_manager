import json

import pytest

from orders.forms import OrderForm, OrderUpdateForm


class TestOrderForms:
    @pytest.mark.parametrize('items_json,valid', [
        (json.dumps({'Burger': 500}), True),
        (json.dumps({'Pizza': 700.0}), True),
        ('invalid_json', False),
        (json.dumps({}), False),
    ])
    def test_order_form_validation(self, items_json, valid):
        form = OrderForm(data={
            'table_number': '1',
            'status': 'pending',
            'items_json': items_json
        })
        assert form.is_valid() == valid

    def test_order_update_form(self):
        form = OrderUpdateForm(data={
            'table_number': '2',
            'status': 'ready',
            'items_json': json.dumps({'Salad': 300})
        })
        assert form.is_valid()
