from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, FallOutTransition

from models.order import Order
from models.order_status_enum import OrderStatus


class OrderDetailScreen(Screen):
    current_order = ObjectProperty()

    def __init__(self, order: Order, **kwargs):
        super(OrderDetailScreen, self).__init__(**kwargs)
        self.current_order = order

    def update_order_status(self, status: OrderStatus):
        self.current_order.status = status
        self.manager.update_order(self.current_order)
        for screen in self.manager.screens:
            if hasattr(screen, 'orders') and len(screen.orders) > 0:
                self.manager.transition = FallOutTransition()
                self.manager.current = screen.name
                break
        self.manager.remove_widget(self)
