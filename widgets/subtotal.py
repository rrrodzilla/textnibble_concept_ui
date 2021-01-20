from typing import List
from decimal import Decimal
from kivy.uix.widget import Widget


class Subtotal(Widget):
    def __init__(self, **kwargs):
        self._subtotal: List[str] = []
        self.register_event_type("on_changed")
        super(Subtotal, self).__init__(**kwargs)

    def on_changed(self, *args):
        pass

    def clear(self):
        self._subtotal.clear()
        self.dispatch("on_changed", self.total)

    def get_total(self):
        if len(self._subtotal) is not 0:
            return Decimal("".join(self._subtotal)) / 100
        else:
            return Decimal("0")

    def append(self, val: str):
        self._subtotal.append(val)

    total = property(get_total)
