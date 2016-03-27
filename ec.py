#!/usr/bin/python

from kivy.app import App
from kivy.uix.widget import Widget

class EC(Widget):
    pass

class EntropayCalculatorApp(App):
    def build(self):
        return EC()

if __name__ == '__main__':
    EntropayCalculatorApp().run()
