from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
import random
import string

class FlagScreen(Screen):
    timer_label = StringProperty()
    country_name = StringProperty()
    country_flag = StringProperty()

    def on_enter(self):
        self.time_left = 60

        self.game_cycle() 
        self.start_timer() 
        
    
    def game_cycle(self): 
        self.country = random.choice(MDApp.get_running_app().lista_paises)
        self.country_name = self.country.get("translations").get("spa").get("common")
        print(self.country_name)
        self.country_flag = self.country.get("flags").get("png")

    def start_timer(self):
        self.evento_reloj = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        # Se llama cada segundo 
        self.time_left -= 1
        if self.time_left < 0:
            print("Termino el tiempo")
            self.evento_reloj.cancel()
            self.manager.current = 'result'
        else:
            self.timer_label = '{:02d}:{:02d}'.format(*divmod(self.time_left, 60))

    def go_to_question_screen(self):
        self.evento_reloj.cancel()
        self.manager.current = "result"