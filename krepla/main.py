#!/usr/bin/env python

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


__version__ = '0.1'


class HistoryInput(BoxLayout):
    pass

class Krepla(BoxLayout):
    line_count = 0
    io_history = ObjectProperty(None)
    def run_input(self, command):
        self.line_count += 1
        row = HistoryInput()
        row.line_num = str(self.line_count)
        row.input_text = command
        self.io_history.add_widget(row)


class KreplaApp(App):
    def build(self):
        return Krepla()


if __name__ == '__main__':
    KreplaApp().run()
