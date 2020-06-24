from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

class SignInScreen(Screen):
    
    signin = ObjectProperty(None)
    valign = StringProperty('top')

    def __init__(self, **kwargs):
        super(SignInScreen, self).__init__(**kwargs)
        Window.bind(on_key_down=self._on_keyboard_down)
        self.valign = kwargs.get("valign", "top")
    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:  # 40 - Enter key pressed
            print(keycode)