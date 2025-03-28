from django.urls import path

from .views import (
    order_create,
    order_delete,
    order_detail,
    order_list,
    order_update,
    revenue,
)

urlpatterns = [
    path('', order_list, name='order_list'),
    path('order_create/', order_create, name='order_create'),
    path('order_update/<int:order_id>/', order_update, name='order_update'),
    path('order_delete/<int:order_id>/', order_delete, name='order_delete'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('revenue/', revenue, name='revenue'),
]
