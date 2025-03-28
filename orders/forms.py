import json

from django import forms

from .models import Order


class BaseOrderForm(forms.ModelForm):
    items_json = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Order
        fields = ['table_number', 'status']

    def clean_items_json(self):
        items_json = self.data.get('items_json', '{}')

        if not items_json and hasattr(self, 'instance'):
            items_json = json.dumps(self.instance.items)

        try:
            items_json = items_json.replace(
                '\\u0022', '"').replace('\\"', '"')
            items = json.loads(items_json)

            if not isinstance(items, dict):
                raise forms.ValidationError('Неверный формат данных блюд')

            if not items:
                raise forms.ValidationError('Добавьте хотя бы одно блюдо')

            for item_name, price in items.items():
                if not isinstance(price, (int, float)):
                    raise forms.ValidationError(
                        f'Некорректный формат цены для "{item_name}"'
                    )

                if price <= 0:
                    raise forms.ValidationError(
                        f'Цена для "{item_name}" должна быть положительной'
                    )

            return items

        except json.JSONDecodeError:
            raise forms.ValidationError('Ошибка декодирования JSON')


class OrderForm(BaseOrderForm):
    pass


class OrderUpdateForm(BaseOrderForm):
    pass
