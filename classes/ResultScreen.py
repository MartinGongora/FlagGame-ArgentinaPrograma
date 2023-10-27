from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget, IconLeftWidget

class CountryItem(TwoLineAvatarListItem):
    pass

class ResultScreen(Screen):
    score = StringProperty()

    def on_enter(self):
        self.list_answers = MDApp.get_running_app().list_answers
        self.score = MDApp.get_running_app().score

        results_list = self.ids.results_list
        results_list.clear_widgets()
         
        for answer in self.list_answers:
            country_name = answer.get("country")
            country_answer = answer.get("answer")
            result_image = answer.get("valid")
            country_item = CountryItem(text=f"{country_name}", secondary_text=f"{country_answer}")
            country_item.add_widget(ImageLeftWidget(source=result_image))
            results_list.add_widget(country_item)
    
    def change_screen(self):
        self.manager.current = "start"