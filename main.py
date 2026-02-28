import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import google.generativeai as genai

# API Configuration
API_KEY = "AIzaSyBpu2OteQAg3wPd9lrCM1GDLDpx3gLMMqw"
genai.configure(api_key=API_KEY)

class AppleDoctor(App):
    def build(self):
        self.title = "Apple Doctor - Developer Rahil Afzal"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Display Header
        layout.add_widget(Label(text="APPLE DOCTOR", font_size='30sp', bold=True))
        layout.add_widget(Label(text="Developer: Rahil Afzal", font_size='15sp', color=(0, 1, 0, 1)))
        
        self.result_label = Label(text="Click to Scan Apple Tree\n(Identify Variety & Pesticide)", halign="center")
        layout.add_widget(self.result_label)
        
        # Buttons
        btn_cam = Button(text="Open Live Camera", size_hint=(1, 0.2), background_color=(0.1, 0.7, 0.1, 1))
        btn_gal = Button(text="Upload from Gallery", size_hint=(1, 0.2), background_color=(0.1, 0.5, 0.8, 1))
        
        btn_cam.bind(on_press=self.analyze_logic)
        btn_gal.bind(on_press=self.analyze_logic)
        
        layout.add_widget(btn_cam)
        layout.add_widget(btn_gal)
        
        return layout

    def analyze_logic(self, instance):
        self.result_label.text = "AI is Analyzing...\nChecking Kashmir Varieties & Dose..."
        # Note: Actual AI analysis happens here using Gemini API
        # Sample Output for UI test:
        self.result_label.text = "Variety: Ambri (Kashmir)\nDisease: Apple Scab\nPesticide: Mancozeb\nDose: 2g per 1 Litre"

if __name__ == "__main__":
    AppleDoctor().run()
