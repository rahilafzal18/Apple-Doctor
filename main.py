from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class AppleDoctor(App):
    def build(self):
        # Background color set karna (optional)
        Window.clearcolor = (0.1, 0.1, 0.1, 1) 
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Developer Name Label
        dev_label = Label(
            text="Developer: Rahil Afzal",
            font_size='24sp',
            color=(0, 1, 0, 1), # Green color
            size_hint=(1, 0.2)
        )
        
        # Main Welcome Label
        welcome_label = Label(
            text="Welcome to Apple Doctor\nNCRT Solution App",
            font_size='20sp',
            halign='center'
        )
        
        layout.add_widget(dev_label)
        layout.add_widget(welcome_label)
        
        return layout

if __name__ == "__main__":
    AppleDoctor().run()
