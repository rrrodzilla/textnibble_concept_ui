from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from order import Order


class LiveOrdersScreen(Screen):
    screen_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super(LiveOrdersScreen, self).__init__(**kwargs)

    def load_orders(self, orders: []):
        for order_obj in orders:
            self.ids.main_layout.add_widget(Order(order_obj))

    def add_order(self):
        self.ids.main_layout.add_widget(Order())
