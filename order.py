from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from typing import List


class Order(BoxLayout):
    # is_complete = BooleanProperty(False)
    # is_empty = BooleanProperty(True)
    # max_size = NumericProperty(4)

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        # self.register_event_type('on_clear')

    # def on_clear(self):
    #     pass

