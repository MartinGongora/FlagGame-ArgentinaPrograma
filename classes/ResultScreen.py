from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import StringProperty

class ResultScreen(Screen):
    score = StringProperty()

    def on_enter(self):
        print(MDApp.get_running_app().score)
        self.score = MDApp.get_running_app().score