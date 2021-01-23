from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from widgets.subtotal import Subtotal
from widgets.numpad import Numpad
from kivy.uix.behaviors import ButtonBehavior


class SubtotalEditor(ButtonBehavior, BoxLayout):
    heading_text = StringProperty(rebind=True)
    subtotal_text = StringProperty(rebind=True)
    subtotal = ObjectProperty(rebind=True)
    show_entry_button = BooleanProperty(False, rebind=True)

    def __init__(self, **kwargs):
        self.register_event_type("on_updated")
        self.subtotal = Subtotal()
        self.subtotal.bind(on_changed=self.update)
        self.numpad = Numpad()
        self.numpad.id = "numpad"
        self.numpad.bind(on_key_pressed=self.set_price_subtotal)
        self.numpad.bind(on_done_pressed=self.toggle_num_pad)
        self.show_numpad = False
        super(SubtotalEditor, self).__init__(**kwargs)

    def on_updated(self, *args):
        pass

    def on_press(self):
        print("pressed")
        if self.show_entry_button:
            self.toggle_num_pad()

    def set_price_subtotal(self, value, *args):
        if args[0] == "[font=Icons]\uef00[/font]":
            self.subtotal.clear()
        else:
            self.subtotal.append(args[0])

    def update(self, *args):
        self.dispatch("on_updated")
        prop = self.property("subtotal")
        prop.dispatch(self)

    def set_value(self, value, *args):
        self.subtotal.clear()
        for letter in [char for char in value]:
            self.subtotal.append(letter)

    def toggle_num_pad(self, *args):
        self.show_numpad = not self.show_numpad
        root = self.get_root_window()
        if self.show_numpad:
            self.numpad.pos = (
                self.pos[0] + ((self.width - self.numpad.minimum_width) / 2),
                self.pos[1] - self.numpad.minimum_height - 12,
            )
            self.numpad.size_hint = None, None
            root.add_widget(self.numpad)
        else:
            root.remove_widget(self.numpad)
