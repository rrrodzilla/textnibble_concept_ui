from abc import abstractmethod

from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.uix.screenmanager import Screen

from order import Order
from ordermanager import OrderManager


class LiveOrdersScreen(Screen):
    screen_manager = ObjectProperty()
    order_manager = ObjectProperty(OrderManager())
    num_orders = NumericProperty()
    # orders = ListProperty()

    def __init__(self, **kwargs):
        super(LiveOrdersScreen, self).__init__(**kwargs)
        self.order_manager.bind(on_loaded=lambda mgr: self.load_orders(mgr.orders))
        # self.order_manager.load_dummy_orders()

    def on_kv_post(self, base_widget):
        self.order_manager.load_dummy_orders()

    def go_to_order_detail_screen(self):
        self.screen_manager.current = 'order_detail'

    @abstractmethod
    def get_filtered_order_list(self, orders):
        return list(orders)

    def load_orders(self, orders):
        print(f'load order widgets from liveordersscreen for {self.name}')
        self.ids.main_layout.clear_widgets()
        _orders = self.get_filtered_order_list(orders)
        _orders = sorted(_orders, key=lambda o: o.time)
        self.num_orders = len(_orders)
        print(f'from load_orders in {self.name}')
        print(self.num_orders)
        for order_obj in _orders:
            order_widget = Order(order_obj)
            order_widget.bind(on_press=(lambda x: self.go_to_order_detail_screen()))
            self.ids.main_layout.add_widget(order_widget)

    def add_order(self):
        self.ids.main_layout.add_widget(Order())
