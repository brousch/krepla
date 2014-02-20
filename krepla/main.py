#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


__version__ = '0.1'


class Krepla(BoxLayout):
    pass


class KreplaApp(App):
    def build(self):
        return Krepla()


if __name__ == '__main__':
    KreplaApp().run()
