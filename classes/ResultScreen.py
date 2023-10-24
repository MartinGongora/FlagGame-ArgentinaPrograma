from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem

class CountryItem(OneLineAvatarListItem):
    pass

class ResultScreen(Screen):
    score = StringProperty()

    def on_enter(self):
        print(MDApp.get_running_app().score)
        print(MDApp.get_running_app().list_answers)
        self.list_answers = MDApp.get_running_app().list_answers
        self.score = MDApp.get_running_app().score
        results_list = self.ids.results_list
        results_list.clear_widgets() 
        for answer in self.list_answers:
            country_name = answer.get("country")
            result = answer.get("valid")
            country_item = CountryItem(text=f"{country_name} - Correcto?: {result}")

            results_list.add_widget(country_item)