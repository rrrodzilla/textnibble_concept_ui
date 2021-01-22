from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from widgets.subtotal import Subtotal
from widgets.numpad import Numpad


class SubtotalEditor(BoxLayout):
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
        self.show_numpad = False
        super(SubtotalEditor, self).__init__(**kwargs)

    def on_updated(self, *args):
        pass

    def update(self, *args):
        self.dispatch("on_updated")
        prop = self.property("subtotal")
        prop.dispatch(self)

    def set_value(self, value):
        self.subtotal.clear()
        for letter in [char for char in value]:
            self.subtotal.append(letter)

    def toggle_num_pad(self, *args):
        self.show_numpad = not self.show_numpad
        if self.show_numpad:
            self.numpad.pos = (
                self.pos[0] + ((self.width - self.numpad.minimum_width) / 2),
                self.pos[1] - self.numpad.minimum_height - 12,
            )
            self.numpad.size_hint = None, None
            self.ids.numpad_layout.add_widget(self.numpad)
        else:
            self.ids.numpad_layout.remove_widget(self.numpad)
