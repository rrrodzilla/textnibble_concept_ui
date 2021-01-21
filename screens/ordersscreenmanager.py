from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import (
    ScreenManager,
    CardTransition,
    SwapTransition,
    WipeTransition,
    SlideTransition,
    RiseInTransition,
)

from datamanagers.ordermanager import OrderManager
from models.order import Order
from screens.orderdetailscreen import OrderDetailScreen


class OrdersScreenManager(ScreenManager):
    order_manager = ObjectProperty(rebind=True)

    def __init__(self, **kwargs):
        self.order_manager = OrderManager()
        super().__init__(**kwargs)

    def edit_order(self, order: Order):
        # TODO get rid of debug print
        # print(f'Editing order for {order.customer_name}')
        self.order_manager.current_order = order
        self.transition = RiseInTransition()
        self.current = "order_detail"

    def update_order(self, order):
        self.order_manager.update_order(order)

    def nav(self, screen_name):
        self.transition = SlideTransition()
        self.current = screen_name
