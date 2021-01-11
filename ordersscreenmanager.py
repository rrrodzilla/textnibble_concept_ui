from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

from datamanagers.ordermanager import OrderManager


class OrdersScreenManager(ScreenManager):
    order_manager = ObjectProperty(OrderManager())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_orders_loaded')
        self.order_manager.bind(on_updated=lambda mgr: self.update_children())

    def on_orders_loaded(self, *args):
        # print(f'{len(self.order_manager.orders())} orders have been loaded')
        pass

    def update_children(self):
        self.canvas.ask_update()
        print('updating children')
