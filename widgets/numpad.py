from kivy.properties import BooleanProperty
from kivy.uix.gridlayout import GridLayout


class Numpad(GridLayout):
    disabled = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Numpad, self).__init__(**kwargs)
        print("registering on_key_pressed in Numpad")
        self.register_event_type("on_key_pressed")

    def on_key_pressed(self, val):
        print("key pressed from Numpad")
        pass