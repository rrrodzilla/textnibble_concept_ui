from kivy.properties import StringProperty
from kivy.uix.button import Button


class KeypadButton(Button):
    def __init__(self, **kwargs):
        super(KeypadButton, self).__init__(**kwargs)

    key_val = StringProperty(None)


