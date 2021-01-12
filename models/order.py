from datetime import datetime

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, NumericProperty

from models.order_status_enum import OrderStatus


class Order(EventDispatcher):
    status = ObjectProperty(OrderStatus.NEW, rebind=True)

    def __init__(self, **kwargs):
        self.id: str
        self.time: datetime
        self.customer_name: str = ''
        self.order_message: str = ''
        self.register_event_type('on_updated')
        super(Order, self).__init__(**kwargs)
        # self.status = OrderStatus.NEW

    def __repr__(self):
        return "Order Object"

    def on_status(self, instance, value):
        print(f'status changed to {value}')
        self.dispatch('on_updated', value)

    def on_updated(self, *args):
        pass
