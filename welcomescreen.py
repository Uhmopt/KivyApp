from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, StringProperty
from kivy.event import EventDispatcher
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from json import dumps
import os.path

# Load the kv files
folder = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(folder + "/homescreen.kv")
Builder.load_file(folder + "/logout.kv")
Builder.load_file(folder + "/spinnerscreen.kv")

from homescreen import HomeScreen
from spinnerscreen import SpinnerScreen
from logout import Logout

class WelcomeScreen(Screen, EventDispatcher):
    refresh_token = ""
    logout_success = BooleanProperty(False)  # Called upon successful sign out
    refresh_token_file = App.get_running_app().user_data_dir + "/refresh_token.txt"
    
    def on_logout_success(self, *args):
        """Overwrite this method to switch to your app's home screen.
        """
        print("Logged out successfully", "<Screen name='firebase_login_screen'>, True") 
    
    def create_refresh_token(self, refresh_token):
        """Saves the refresh token in a local file to enable automatic sign in
        next time the app is opened.
        """
        if os.path.exists(refresh_token):
            print("The file exists")            
        else:
            f = open(refresh_token, "x")   

    def log_out(self):
        """Overwrite this method to switch to your app's home screen.
        """
        if os.path.exists(self.refresh_token_file):
            os.remove(self.refresh_token_file)
        self.create_refresh_token(self.refresh_token_file)
        self.logout_success = True

