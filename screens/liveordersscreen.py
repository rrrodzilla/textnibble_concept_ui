from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen

from order import Order


class LiveOrdersScreen(Screen):
    orders = ListProperty(rebind=True)

    def __init__(self, **kwargs):
        super(LiveOrdersScreen, self).__init__(**kwargs)

    def go_to_order_detail_screen(self):
        self.manager.current = 'order_detail'

    def on_orders(self, instance, value):
        self.ids.main_layout.clear_widgets()
        _orders = sorted(self.orders, key=lambda o: o.time)
        for order_obj in _orders:
            order_widget = Order(order_obj)
            order_widget.bind(on_press=(lambda x: self.go_to_order_detail_screen()))
            self.ids.main_layout.add_widget(order_widget)
