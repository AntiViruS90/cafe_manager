import json

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import OrderForm, OrderUpdateForm
from .models import Order


def order_list(req):
    orders = Order.objects.all()

    table_number = req.GET.get('table_number')
    status = req.GET.get('status')

    if table_number:
        orders = orders.filter(table_number__icontains=table_number)

    if status:
        orders = orders.filter(status__iexact=status)

    return render(req, 'orders/order_list.html', {
        'orders': orders,
        'req': req,
    })


def order_create(req):
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.items = form.cleaned_data['items_json']
            form.save()
            return redirect('order_list')
        else:
            print("Ошибка валидации", form.errors)
    else:
        form = OrderForm()
    return render(req, 'orders/order_create.html', {
        'form': form,
        'initial_items_json': '{}'
    })


def order_update(req, order_id):
    order = get_object_or_404(Order, id=order_id)

    if req.method == 'POST':
        form = OrderUpdateForm(req.POST, instance=order)

        if form.is_valid():
            order = form.save(commit=False)

            items_json = req.POST.get('items_json', '{}')
            try:
                items_data = json.loads(items_json)

                if not all(
                        isinstance(
                        price, (int, float)
                        ) for name, price in items_data.items()):
                    raise ValueError("Цены должны быть числами")
                order.items = items_data
            except (ValueError, TypeError) as e:
                print("Ошибка обработки блюд:", e)

            order.save()
            return redirect('order_list')
    else:
        form = OrderUpdateForm(instance=order)

    items_list = [
        {'name': name, 'price': price} for name, price in order.items.items()
    ]
    items_json = json.dumps(order.items)

    return render(req, 'orders/order_update.html', {
        'form': form,
        'order': order,
        'items': items_list,
        'items_json': items_json,
        'initial_items_json': json.dumps(order.items)  # Для инициализации JS
    })


def order_delete(req, order_id):
    order = get_object_or_404(Order, id=order_id)

    if req.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(req, 'orders/order_confirm_delete.html', {'order': order})


def order_detail(req, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(req, 'orders/order_detail.html', {'order': order})


def revenue(req):
    total_revenue = Order.objects.filter(
        status='paid').aggregate(Sum('total_price'))['total_price__sum'] or 0
    return render(req, 'orders/revenue.html', {'total_revenue': total_revenue})
