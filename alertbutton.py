from time import sleep

from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex as c


class AlertButton(FloatLayout):
    badge_total = NumericProperty(rebind=True)
    button_text = StringProperty(rebind=True)
    button_color = ObjectProperty(c('#E4E4E7'))
    badge_color = ObjectProperty(c('#E4E4E7'))
    urgent = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(AlertButton, self).__init__(**kwargs)
        self.register_event_type('on_press')
        self.size_hint = 0, 1
        self.opacity = 0
        self.badgeEvent = None
        # if self.badge_total == 0:
        #     self.size_hint = None, None

    def on_press(self):
        pass

    def on_badge_total(self, instance, value):
        print(f'updating badge to: {value} for {self.button_text}')
        self.ids.alert.text = str(value)
        if value > 0:
            # animate button fly out
            animation = Animation(size_hint=(.15, 1), t='in_out_cubic', duration=.25)
            animation &= Animation(opacity=1, duration=.35)
            animation.bind(on_complete=self.animate_badge)
            animation.start(self)
        else:
            self.size_hint = 0, 1
            self.opacity = 0
        self.canvas.ask_update()
        # self.canvas.ask_update()

    def animate_badge(self, *args):
        # animate badge pop up
        if self.badgeEvent is not None:
            self.badgeEvent.cancel()
        print('animating badge')
        self.ids.alert.size = (0, 0)
        self.ids.alert.opacity = 0
        badge_anim = Animation(size=(24, 24), t='out_bounce', duration=.3)
        badge_anim &= Animation(opacity=1, t='out_cubic', duration=.35)
        badge_anim.repeat = self.urgent
        badge_anim.start(self.ids.alert)
        if self.urgent:
            self.badgeEvent = Clock.schedule_interval(self.animate_badge, 6)

