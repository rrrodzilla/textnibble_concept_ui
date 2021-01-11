from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.widget import Widget
from typing import List


class PinNumber(Widget):
    is_complete = BooleanProperty(False)
    is_empty = BooleanProperty(True)
    max_size = NumericProperty(4)

    def __init__(self, **kwargs):
        super(PinNumber, self).__init__(**kwargs)
        self.register_event_type('on_clear')
        self.register_event_type('on_complete')
        self.register_event_type('on_add_digit')
        self.pin: List[int] = []

    def on_complete(self):
        pass

    def add_digit(self, val: int):

        if not self.is_complete:
            # print('adding digi')
            self.pin.append(val)
            self.is_empty = False
        # else:
        #     print('NOT adding digi')
        self.is_complete = not (len(self.pin) < self.max_size)
        if self.is_complete:
            self.dispatch('on_complete')
        # print(f"\nPin length: {len(self.pin)}")
        # print(f"Max Size: {self.max_size}")
        # print(f"is_complete: {self.is_complete}")
        self.dispatch('on_add_digit')

    def clear(self):
        # print("clearing pin")
        self.pin.clear()
        self.is_complete = False
        self.dispatch('on_clear')
        self.is_empty = True

    def on_clear(self):
        pass

    def on_add_digit(self):
        pass
