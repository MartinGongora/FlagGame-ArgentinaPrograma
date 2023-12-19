from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock
import random


class FlagScreen(Screen):
    timer_label = StringProperty()
    country_name = StringProperty()
    country_flag = StringProperty()
    answer = StringProperty()

    def on_enter(self):
        self.time_left = 60
        self.score = 0
        self.game_cycle() 
        self.start_timer() 
        self.list_answers = []
        
    
    def game_cycle(self): 
        self.country = random.choice(MDApp.get_running_app().lista_paises)
        self.country_name = self.country.get("translations").get("spa").get("common")
        self.country_flag = self.country.get("flags").get("png")
        self.correct_answer = self.normalize(self.country_name.upper())
        print(self.correct_answer)
    
    def check_answer(self, instance):
        # Se verifica si el boton presionado contiene la respuesta correcta
        self.country_answer = self.normalize(instance.text.upper())
        if(len(self.country_answer)==0):
            self.country_answer = " "
        if self.country_answer == self.correct_answer:
            print("Acierto!")
            self.score += 1
            self.respuesta = {"country": self.country_name, "answer": self.country_answer,"valid": "resources/correct.png"}
            self.list_answers.append(self.respuesta)
        else:
            self.respuesta = {"country": self.country_name, "answer": self.country_answer,"valid": "resources/incorrect.png"}
            self.list_answers.append(self.respuesta)            
        self.ids.id_text_field.text = "" 
        self.game_cycle()   

    def start_timer(self):
        self.evento_reloj = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        # Se llama cada segundo 
        self.time_left -= 1
        if self.time_left < 0:
            print("Termino el tiempo")
            MDApp.get_running_app().score = str(self.score)
            print(self.score)
            MDApp.get_running_app().list_answers = self.list_answers
            self.go_to_question_screen()
        else:
            self.timer_label = '{:02d}:{:02d}'.format(*divmod(self.time_left, 60))

    def go_to_question_screen(self):
        self.evento_reloj.cancel()
        self.manager.current = "result"

    def normalize(self, s):
        replacements = (
            ("Á", "A"),
            ("É", "E"),
            ("Í", "I"),
            ("Ó", "O"),
            ("Ú", "U")
        )
        for a, b in replacements:
            s = s.replace(a,b)
        return s