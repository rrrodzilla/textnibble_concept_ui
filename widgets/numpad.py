from kivy.properties import BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class Numpad(BoxLayout):
    disabled = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(Numpad, self).__init__(**kwargs)
        print("registering on_key_pressed in Numpad")
        self.orientation = "vertical"
        self.register_event_type("on_done_pressed")
        self.register_event_type("on_key_pressed")

    def on_key_pressed(self, val):
        print(f"key pressed from Numpad: {val}")
        pass

    def on_done_pressed(self, val):
        pass
