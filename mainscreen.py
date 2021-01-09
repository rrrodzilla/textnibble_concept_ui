from operator import itemgetter

from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from datetime import datetime, timezone
from models.order import Order as orderObj
from dateutil.relativedelta import relativedelta
import random
from faker import Faker

from models.order_status_enum import OrderStatus

fake = Faker()


class Mainscreen(Screen):
    orders = ListProperty()
    active_orders = ListProperty()

    def __init__(self, **kwargs):
        super(Mainscreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.load_orders()
        self.sort_orders_by_time()
        self.ids.live_orders.load_orders(self.orders)
        active_order_list = self.get_active_orders()
        self.ids.active_orders.load_orders(active_order_list)
        self.ids.num_orders.text = str(self.ids.active_orders.num_orders)

    def get_active_orders(self):
        return list(filter(lambda r: r.status is OrderStatus.NEW or r.status is OrderStatus.PAID
                                         or r.status is OrderStatus.UPDATED, self.orders))

    def sort_orders_by_time(self):
        return self.orders.sort(key=lambda o: o.time)

    def load_orders(self):
        count = 0
        self.orders.clear()
        while count < random.randint(10, 30):
            new_order = orderObj()
            new_order.customer_name = fake.name()
            new_order.status = OrderStatus(random.randint(OrderStatus.NEW.value, OrderStatus.FULFILLED.value))
            if new_order.status is OrderStatus.NEW:
                new_order.time = datetime.now(tz=timezone.utc)
            else:
                new_order.time = datetime.now(tz=timezone.utc) + relativedelta(minutes=-random.randint(2, 15))
            new_order.order_message = fake.sentence()
            self.orders.append(new_order)
            count = count + 1
