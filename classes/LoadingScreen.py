from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import time

class LoadingScreen(Screen):

    def on_enter(self):
        while len(MDApp.get_running_app().lista_paises)==0:
            time.sleep(1)
        self.change_screen()

    def change_screen(self):
        self.manager.current = "flags"