from kivy.uix.screenmanager import Screen

from order import Order


class LiveOrdersScreen(Screen):
    def add_order(self):
        self.ids.main_layout.add_widget(Order())
