from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform
from kivy.lang import Builder
import threading

from classes.StartScreen import StartScreen
from classes.ApiConection import ApiConection
from classes.FlagScreen import FlagScreen

Builder.load_file('GUI/StartScreen.kv')

class FlagGameApp(MDApp):
    # Variables globales a la App
    lista_paises = []
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        t = threading.Thread(target=self.api_conection)
        t.start()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(FlagScreen(name="flags"))
        return sm
    
    def api_conection(self):
        api = ApiConection()
        self.lista_paises = ApiConection.search_product(api)
        print(self.lista_paises[1])


if __name__ == '__main__':
    FlagGameApp().run()