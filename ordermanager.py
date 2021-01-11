import random
from datetime import datetime, timezone

from faker import Faker
from dateutil.relativedelta import relativedelta
from kivy.properties import BooleanProperty, NumericProperty, ListProperty
from kivy.uix.widget import Widget

from models.order import Order as orderObj
from typing import List

from models.order_status_enum import OrderStatus
from singleton import Singleton

fake = Faker()


class OrderManager(Widget):
    __metaclass__ = Singleton
    orders = ListProperty()

    def __init__(self, **kwargs):
        super(OrderManager, self).__init__(**kwargs)
        self.register_event_type('on_loaded')
        self.register_event_type('on_clear')

    def clear(self):
        self.orders.clear()
        self.dispatch('on_clear')

    def on_clear(self):
        pass

    def on_loaded(self, *args):
        pass

    def load_dummy_orders(self):
        count = 0
        self.clear()

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
        self.dispatch('on_loaded')
