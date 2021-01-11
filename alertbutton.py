from kivy.properties import StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class AlertButton(FloatLayout):
    badge_total = NumericProperty(rebind=True)
    button_text = StringProperty(rebind=True)

    def __init__(self, **kwargs):
        super(AlertButton, self).__init__(**kwargs)
        self.register_event_type('on_press')

    def on_press(self):
        pass

    def on_badge_total(self, instance, value):
        print(f'updating badge to: {value}')
        self.ids.alert.text = str(value)
        # self.canvas.ask_update()
