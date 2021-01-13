from datetime import datetime

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, NumericProperty

from models.order_status_enum import OrderStatus


class Employee(EventDispatcher):
    # status = ObjectProperty(OrderStatus.NEW, rebind=True)

    def __init__(self, **kwargs):
        self.id: str
        self.name: str
        self.pin: str
        super(Employee, self).__init__(**kwargs)

    def __repr__(self):
        return "Employee Object"

