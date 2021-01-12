from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from datamanagers.ordermanager import OrderManager
from models.order import Order
from screens.orderdetailscreen import OrderDetailScreen


class OrdersScreenManager(ScreenManager):
    order_manager = ObjectProperty(OrderManager())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def edit_order(self, order: Order):
        detail_screen = OrderDetailScreen(order)
        self.add_widget(detail_screen)
        self.current = 'order_detail'

    def update_order(self, order):
        self.order_manager.update_order(order)

