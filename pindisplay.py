from kivy.uix.boxlayout import BoxLayout

from pincharacter import PinCharacter


class PinDisplay(BoxLayout):
    def __init__(self, **kwargs):
        super(PinDisplay, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.max_size = 0

    def set_max_size(self, max_size: int):
        count = 0
        self.clear_widgets()
        while count < max_size:
            char = PinCharacter()
            char.disabled = True
            self.add_widget(char)
            count = count + 1

    def enable(self, how_many: int):
        count = 0
        while count < how_many:
            self.children[len(self.children)-how_many].disabled = False
            count = count + 1
