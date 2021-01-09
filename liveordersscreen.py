from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from order import Order


class NumberProperty(object):
    pass


class LiveOrdersScreen(Screen):
    screen_manager = ObjectProperty()
    num_orders = NumberProperty()

    def __init__(self, **kwargs):
        super(LiveOrdersScreen, self).__init__(**kwargs)

    def go_to_order_detail_screen(self):
        self.screen_manager.current = 'order_detail'

    def load_orders(self, orders: []):
        self.ids.main_layout.clear_widgets()
        for order_obj in orders:
            order_widget = Order(order_obj)
            order_widget.bind(on_press=(lambda x: self.go_to_order_detail_screen()))
            self.ids.main_layout.add_widget(order_widget)
        self.num_orders = len(orders)

    def add_order(self):
        self.ids.main_layout.add_widget(Order())
