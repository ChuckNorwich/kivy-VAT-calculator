import kivy
from  kivy.config import Config
MAX_SIZE = (350, 550)
Config.set('graphics', 'width', MAX_SIZE[0])
Config.set('graphics', 'height', MAX_SIZE[1])


from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from  kivy.uix.button import Button
from  kivy.uix.widget import Widget
from  kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from  kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from plyer import gps
from kivy.clock import Clock, mainthread


class Gui(Widget):
    net = ObjectProperty(None)
    vat = ObjectProperty(None)
    total = ObjectProperty(None)

    def calculate(self):
        print('Net: ', self.net.text, 'VAT: ', self.vat.text, 'Total: ', self.total.text)



    def clear(self):
        self.net.text = ' '
        self.vat.text = ' '
        self.total.text = ' '




class VatApp(App):
    title = 'UK VAT Calculator'
    def build(self):
        return Gui()


if __name__ == "__main__":
    VatApp().run()
