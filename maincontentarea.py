from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

from liveordersscreen import LiveOrdersScreen
from previousordersscreen import PreviousOrdersScreen


class MainContentArea(ScreenManager):
    def __init__(self, **kwargs):
        super(MainContentArea, self).__init__(**kwargs)
        self.add_widget(LiveOrdersScreen(name='live_orders'))
        self.add_widget(PreviousOrdersScreen(name='previous_orders'))
        self.current = "live_orders"
        # self.add_widget(sm)
    # def on_pre_enter(self, *args):
    #     sm = ScreenManager(transition=FadeTransition())
    #     sm.add_widget(LiveOrdersScreen(name='live_orders'))
    #     sm.add_widget(PreviousOrdersScreen(name='previous_orders'))
