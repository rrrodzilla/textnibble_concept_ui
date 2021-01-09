from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from liveordersscreen import LiveOrdersScreen
from models.order_status_enum import OrderStatus
from order import Order


class ActiveOrdersScreen(LiveOrdersScreen):

    def __init__(self, **kwargs):
        super(ActiveOrdersScreen, self).__init__(**kwargs)
