from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from widgets.subtotal import Subtotal


class SubtotalEditor(BoxLayout):
    heading_text = StringProperty(rebind=True)
    subtotal_text = StringProperty(rebind=True)
    subtotal = ObjectProperty(rebind=True)

    def __init__(self, **kwargs):
        self.register_event_type("on_updated")
        self.subtotal = Subtotal()
        self.subtotal.bind(on_changed=self.update)
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
