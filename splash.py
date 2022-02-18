from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock

Window.size = (300,500)

class SplashScreenApp(MDApp):
    def build(self):
        global sm 
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        return sm
    def on_start(self):
        Clock.schedule_once(self.login, 5)
        
    def login(*args):
        sm.current = "login" 
        
if __name__=="__main__":
    SplashScreenApp().run()