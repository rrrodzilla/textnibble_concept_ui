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
        # if self.badge_total == 0:
        #     self.size_hint = None, None

    def on_press(self):
        pass

    def on_badge_total(self, instance, value):
        print(f'updating badge to: {value}')
        self.ids.alert.text = str(value)
        # if value > 0:
        #     print(f'updating button size')
        #     self.size_hint = 1, 1
        # else:
        #     self.size_hint = None, None
        # self.canvas.ask_update()
        # self.canvas.ask_update()
