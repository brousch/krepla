from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
 
 
kv = """
<Test>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, None
        Button:
            text: "1"
            size_hint: None, 1
            width: 16
        Label:
            height: self.texture_size[1]
            id: output_label
            size_hint: 1, None
            text: "This button is 16px wide"
            text_size: self.width, None
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, None
        Button:
            text: "1"
            size_hint: None, 1
            width: 8
        Label:
            height: self.texture_size[1]
            size_hint: 1, None
            text: "This button is 8px wide"
            text_size: self.width, None
    Label:
        text: "This is here to get the others above Inspector"
    
"""
 
Builder.load_string(kv)
 
 
class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)
 
 
class TestApp(App):
    def build(self):
        return Test()
 
if __name__ == '__main__':
    TestApp().run()
    
    