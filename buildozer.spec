import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
import google.generativeai as genai

# --- API KEY SETTING ---
API_KEY = "AIzaSyBpu2OteQAg3wPd9lrCM1GDLDpx3gLMMqw"
genai.configure(api_key=API_KEY)

class AppleDoctorApp(App):
    def build(self):
        self.title = "Apple Doctor - Developer Rahil Afzal"
        
        # Main Layout
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Header Section
        header = BoxLayout(orientation='vertical', size_hint=(1, 0.2))
        header.add_widget(Label(text="APPLE DOCTOR", font_size='32sp', color=(1, 1, 1, 1), bold=True))
        header.add_widget(Label(text="Developer: Rahil Afzal", font_size='16sp', color=(0, 1, 0, 1)))
        root.add_widget(header)

        # Result Display (Scrollable for long pesticide instructions)
        scroll = ScrollView(size_hint=(1, 0.4))
        self.status = Label(
            text="Welcome!\n1. Click Camera to Scan\n2. Click Gallery to Upload\n\nAI will identify Kashmir Varieties & Pesticide Dose.",
            halign="center", valign="middle", size_hint_y=None, text_size=(400, None)
        )
        self.status.bind(texture_size=self.status.setter('size'))
        scroll.add_widget(self.status)
        root.add_widget(scroll)
        
        # Buttons Section
        buttons = BoxLayout(orientation='vertical', size_hint=(1, 0.4), spacing=10)
        
        btn_camera = Button(text="[ LIVE CAMERA SCAN ]", font_size='18sp', background_color=(0.1, 0.8, 0.1, 1))
        btn_gallery = Button(text="[ UPLOAD FROM GALLERY ]", font_size='18sp', background_color=(0.1, 0.5, 0
