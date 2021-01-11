import random
from datetime import datetime, timezone

from dateutil.relativedelta import relativedelta
from faker import Faker
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.widget import Widget

from datamanagers.orderfilterabstract import OrderFilterAbstract
from datamanagers.orderfilteractive import OrderFilterActive
from datamanagers.orderfilterawaitingpickup import OrderFilterAwaitingPickup
from datamanagers.orderfilterfullfilled import OrderFilterFulfilled
from datamanagers.orderfilteridle import OrderFilterIdle
from datamanagers.orderfilterworking import OrderFilterWorking
from descriptors.lazyproperty import LazyProperty
from models.order import Order as orderObj
from models.order_status_enum import OrderStatus
from singleton import Singleton

fake = Faker()


class OrderManager(Widget):
    __metaclass__ = Singleton
    all_orders = ListProperty(rebind=True)
    urgent_orders = ListProperty(rebind=True)
    working_orders = ListProperty(rebind=True)
    idle_orders = ListProperty(rebind=True)
    awaiting_pickup_orders = ListProperty(rebind=True)
    fulfilled = ListProperty(rebind=True)

    def __init__(self, **kwargs):
        super(OrderManager, self).__init__(**kwargs)
        self.register_event_type('on_loaded')
        self.register_event_type('on_updated')
        self.register_event_type('on_clear')
        # self.load_dummy_orders()

    def on_updated(self, *args):
        pass

    def clear(self):
        self.all_orders.clear()
        self.dispatch('on_clear')

    def on_clear(self):
        pass

    def on_loaded(self, *args):
        pass

    def on_all_orders(self, instance, value):
        self.all_orders = value
        self.urgent_orders = OrderFilterActive().Filter(value)
        self.working_orders = OrderFilterWorking().Filter(value)
        self.idle_orders = OrderFilterIdle().Filter(value)
        self.awaiting_pickup_orders = OrderFilterAwaitingPickup().Filter(value)
        self.fulfilled = OrderFilterFulfilled().Filter(value)

    def add_dummy_order(self):
        # print('adding order')
        new_order = orderObj()
        new_order.customer_name = fake.name()
        new_order.status = OrderStatus(random.randint(OrderStatus.NEW.value, OrderStatus.FULFILLED.value))
        if new_order.status is OrderStatus.NEW:
            new_order.time = datetime.now(tz=timezone.utc)
        else:
            new_order.time = datetime.now(tz=timezone.utc) + relativedelta(minutes=-random.randint(2, 15))
        new_order.order_message = fake.sentence()
        self.all_orders.append(new_order)

    def load_dummy_orders(self):
        count = 0
        self.clear()

        while count < random.randint(10, 30):
            self.add_dummy_order()
            count = count + 1
        self.dispatch('on_loaded')

