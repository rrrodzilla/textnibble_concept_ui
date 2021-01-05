from kivy.animation import Animation, AnimationTransition
from kivy.clock import Clock
from kivy.properties import BooleanProperty, NumericProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex as c
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from typing import List


class Order(ButtonBehavior, BoxLayout):
    # is_complete = BooleanProperty(False)
    # is_empty = BooleanProperty(True)
    # max_size = NumericProperty(4)
    accent_color = ObjectProperty(c('#22D3EE'))

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        pass

    def on_press(self):
        print('testing press from order')
        return True
        # pass

    #     print('starting animmation')
    #     anim = Animation(pos=(self.x, y), duration=.2, transition='out_back')
    #     anim.start(self)
    # def on_clear(self):
    #     pass

