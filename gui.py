import kivy

kivy.require("2.1.0")  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class Screen1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Label(text="hello"))
        # self.add_widget(Button(text="test"))s


class MyApp(App):
    def build(self):
        return Screen1


if __name__ == "__main__":
    MyApp().run()
