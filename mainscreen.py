from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from datetime import datetime

from models.order import Order as orderObj


class Mainscreen(Screen):
    orders = ListProperty()

    def __init__(self, **kwargs):
        super(Mainscreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.load_orders()
        self.ids.live_orders.load_orders(self.orders)

    def load_orders(self):
        count = 0
        while count < 10:
            new_order = orderObj()
            new_order.customer_name = "Roland"
            new_order.order_time = datetime.now()
            new_order.order_message = "here's a new order"
            self.orders.append(new_order)
            count = count + 1
