from kivy.uix.screenmanager import Screen

class StartScreen(Screen):
    def change_screen(self):
        self.manager.current = "flags"
    