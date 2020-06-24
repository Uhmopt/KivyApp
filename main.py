from kivy.app import App
from kivy import utils
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

# -- This import can be done in kv lang or python  
class MainApp(App):
    def build(self):
        return self.root

if __name__ == "__main__":
    MainApp().run()