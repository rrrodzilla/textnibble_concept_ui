from kivy.properties import BooleanProperty
from kivy.uix.gridlayout import GridLayout


class Keypad(GridLayout):
    disabled = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(Keypad, self).__init__(**kwargs)
        self.register_event_type('on_key_pressed')

    def on_key_pressed(self, val):
        pass
