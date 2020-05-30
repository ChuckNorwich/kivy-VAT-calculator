import kivy
from  kivy.config import Config
MAX_SIZE = (350, 550)
Config.set('graphics', 'width', MAX_SIZE[0])
Config.set('graphics', 'height', MAX_SIZE[1])


from kivy.app import App


from kivy.uix.widget import Widget
from  kivy.properties import ObjectProperty



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
