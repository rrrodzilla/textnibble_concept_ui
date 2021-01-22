from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex as c


class KeypadButton(Button):
    enabled_color = ObjectProperty(c("#15803D"), rebind=True)
    disabled_color = ObjectProperty(c("#3F3F46"), rebind=True)

    def __init__(self, **kwargs):
        super(KeypadButton, self).__init__(**kwargs)

    key_val = StringProperty(None)
