from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex as c
import arrow
from models.order import Order as OrderModel
from models.order_status_enum import OrderStatus


def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Order(ButtonBehavior, BoxLayout):
    accent_color = ObjectProperty(c('#22D3EE'))
    accent_darker = ObjectProperty(c('#0891B2'))
    order_message = StringProperty()
    customer_name = StringProperty()
    minutes = StringProperty()
    ago = StringProperty()

    def __init__(self, order: OrderModel, **kwargs):
        super(Order, self, **kwargs).__init__(**kwargs)
        self.order_message = order.order_message
        self.customer_name = order.customer_name
        dt = order.time
        adt = arrow.Arrow.fromdatetime(dt)
        self.minutes, self.ago = arrow.Arrow.fromdatetime(order.time).humanize().split(' ', 1)
        if not IsInt(self.minutes):
            self.minutes = ''
            self.ago = '[size=24][b]just\nnow[/b][/size]'
        if order.status is OrderStatus.NEW:
            self.ids.status_label.text = "NEW"
            self.accent_color = c('#DC2626')
        if order.status is OrderStatus.PAID:
            self.ids.status_label.text = "READY FOR KITCHEN"
            self.accent_color = c('#DC2626')
        self.accent_darker = c('#EA580C')
        if order.status is OrderStatus.UPDATED:
            self.ids.status_label.text = "CUSTOMER REPLIED"
            self.accent_color = c('#DC2626')
        if order.status is OrderStatus.AWAITING_REPLY:
            self.ids.status_label.text = "AWAITING REPLY"
            self.accent_color = c('#D4D4D8')
        if order.status is OrderStatus.AWAITING_PICKUP:
            self.ids.status_label.text = "AWAITING PICKUP"
            self.accent_color = c('#D4D4D8')
        if order.status is OrderStatus.AWAITING_PAYMENT:
            self.ids.status_label.text = "AWAITING PAYMENT"
            self.accent_darker = c('#E5E5E5')
        if order.status is OrderStatus.FULFILLED:
            self.ids.status_label.text = "FULFILLED"
            # self.accent_color = c('#84CC16')
            self.accent_color = c('#4D7C0F')
        if order.status is OrderStatus.WORKING:
            self.ids.status_label.text = "KITCHEN"
            self.accent_color = c('#EAB308')

            # self.accent_color = c('#52525B')

        # print(order.status.name)

    def on_press(self):
        pass
