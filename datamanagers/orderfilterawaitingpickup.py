from datamanagers.orderfilterabstract import OrderFilterAbstract
from models.order import Order
from models.order_status_enum import OrderStatus


class OrderFilterAwaitingPickup(OrderFilterAbstract):
    def Filter(self, orders: Order):
        temp_orders = [r for r in orders if r.status is OrderStatus.AWAITING_PICKUP]
        return temp_orders
