import kivy
from kivy import Config
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from loginscreen import LoginScreen
from mainscreen import Mainscreen

kivy.require('2.0.0')


class Controller(FloatLayout):
    """Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    """
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'


class Textnibble(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(Mainscreen(name='main'))

        return sm


if __name__ == '__main__':
    LabelBase.register(name="Inter",
                       fn_regular="./fonts/Inter-Regular.ttf",
                       fn_bold="./fonts/Inter-Black.ttf",
                       fn_italic="./fonts/Inter-Light.ttf",
                       fn_bolditalic="./fonts/Inter-SemiBold.ttf")
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    Textnibble().run()
