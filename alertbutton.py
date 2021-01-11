from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class AlertButton(FloatLayout):
    alert_text = StringProperty()
    button_text = StringProperty()

    def __init__(self, **kwargs):
        super(AlertButton, self).__init__(**kwargs)
        self.register_event_type('on_press')

    def on_press(self):
        pass
