from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform
from kivy.lang import Builder
import threading


from classes.StartScreen import StartScreen
from classes.ApiConection import ApiConection
from classes.FlagScreen import FlagScreen
from classes.ResultScreen import ResultScreen
from classes.LoadingScreen import LoadingScreen

Builder.load_file('GUI/StartScreen.kv')
Builder.load_file('GUI/FlagScreen.kv')
Builder.load_file('GUI/ResultScreen.kv')
Builder.load_file('GUI/LoadingScreen.kv')


class FlagGameApp(MDApp):
    # Variables globales a la App
    lista_paises = []
    score = ""
    list_answers = []
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        t = threading.Thread(target=self.api_conection, daemon=True)
        t.start()

    def build(self):
        sm = ScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(FlagScreen(name="flags"))
        sm.add_widget(ResultScreen(name="result"))
        return sm
    
    def api_conection(self):
        api = ApiConection()
        self.lista_paises = ApiConection.search_countries(api)
        print("Tengo los paises")


if __name__ == '__main__':
    FlagGameApp().run()