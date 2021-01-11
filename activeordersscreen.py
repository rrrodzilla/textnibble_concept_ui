from kivy.properties import NumericProperty

from liveordersscreen import LiveOrdersScreen
from models.order_status_enum import OrderStatus


class ActiveOrdersScreen(LiveOrdersScreen):
    order_total = NumericProperty()

    def __init__(self, **kwargs):
        super(ActiveOrdersScreen, self).__init__(**kwargs)

    # def on_kv_post(self, base_widget):
    #     super().on_kv_post(base_widget)
        # pass

    # def get_filtered_order_list(self, orders):
    #     super().get_filtered_order_list(orders)
    #     temp_orders = [r for r in orders if r.status is OrderStatus.NEW or r.status is OrderStatus.PAID or
    #                             r.status is OrderStatus.UPDATED]
    #     self.order_total = len(temp_orders)
    #     print(f'from get_filtered_order_list in {self.name}')
    #     print(self.order_total)
    #     return temp_orders

