from kivy.properties import NumericProperty

from liveordersscreen import LiveOrdersScreen
from models.order_status_enum import OrderStatus


class WorkingOrdersScreen(LiveOrdersScreen):
    order_total = NumericProperty()

    def get_filtered_order_list(self, orders):
        super().get_filtered_order_list(orders)
        temp_orders = [r for r in orders if r.status is OrderStatus.WORKING]
        self.order_total = len(temp_orders)
        print(f'from get_filtered_order_list in {self.name}')
        print(self.order_total)
        return temp_orders

    def __init__(self, **kwargs):
        super(WorkingOrdersScreen, self).__init__(**kwargs)

