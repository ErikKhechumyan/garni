from kivy.app import App 
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout
import subprocess

video_paths = {
    "armenia": "videos/armenia.mp4",
    "uk": "videos/uk.mp4",
    "russia": "videos/russia.mp4",
    "france": "videos/france.mp4",
    "germany": "videos/germany.mp4",
    "italy": "videos/italy.mp4",
    "spain": "videos/spain.mp4",
    "saudi": "videos/saudi.mp4",
    "iran": "videos/iran.mp4"
}

flag_paths = {
    "armenia": "flags/armenia.png",
    "uk": "flags/uk.png",
    "russia": "flags/russia.png",
    "france": "flags/france.png",
    "germany": "flags/germany.png",
    "italy": "flags/italy.png",
    "spain": "flags/spain.png",
    "saudi": "flags/saudi.png",
    "iran": "flags/iran.png",
}

class ImageButton(ButtonBehavior, Image):
    pass

class MainApp(App):
    def build(self):
        Window.fullscreen = True
        Window.bind(on_key_down=self.on_key_down)

        self.root = FloatLayout()
        self.set_background("backgrounds/background.jpg")

        content = BoxLayout(orientation='vertical', spacing=20, padding=40,
                            size_hint=(.9, .9), pos_hint={"center_x": .5, "center_y": .5})
        self.root.add_widget(content)

        # Верхняя панель
        top_panel = BoxLayout(orientation='horizontal', size_hint=(1, None), height=100, spacing=10)
        top_panel.add_widget(Image(source="icons/left_icon.png", size_hint=(None, None), size=(80, 80)))
        top_panel.add_widget(Label(
            text="ՀՀ ԿԳՄՍ ՆԱԽԱՐԱՐՈՒԹՅՈՒՆ\nՊԱՏՄԱՄՇԱԿՈՒԹԱՅԻՆ ԱՐԳԵԼՈՑ-ԹԱՆԳԱՐԱՆՆԵՐԻ ԵՎ\nՊԱՏՄԱԿԱՆ ՄԻՋԱՎԱՅՐԻ ՊԱՀՊԱՆՈՒԹՅԱՆ ԾԱՌԱՅՈՒԹՅՈՒՆ\nպետական ոչ առևտրային կազմակերպություն ",
            font_size=12, halign="center", valign="middle",font_name='Arial',color=(0, 0, 0, 1)))
        top_panel.add_widget(Image(source="icons/right_icon.png", size_hint=(None, None), size=(80, 80)))
        content.add_widget(top_panel)

        # Флаги (центрирование)
        flag_order = [
            ["armenia", "uk", "russia", "france", "germany"],
            ["italy", "spain", "saudi", "iran"]
        ]

        for row in flag_order:
            anchor = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1, None), height=60)
            row_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), height=60)
            for country in row:
                btn = ImageButton(source=flag_paths[country], size_hint=(None, None), size=(80, 50))
                btn.bind(on_press=lambda instance, c=country: self.play_video(video_paths[c]))
                row_layout.add_widget(btn)
            row_layout.width = len(row) * (80 + 15)
            anchor.add_widget(row_layout)
            content.add_widget(anchor)

        # Нижняя панель
        bottom_panel = BoxLayout(orientation='horizontal', size_hint=(1, None), height=60, padding=[40, 0])
        bottom_panel.add_widget(Image(source="icons/genesis.png", size_hint=(None, None), size=(150, 62)))
        bottom_panel.add_widget(Widget())  
        bottom_panel.add_widget(Image(source="icons/tumo.png", size_hint=(None, None), size=(150, 62)))
        content.add_widget(bottom_panel)

        return self.root

    def set_background(self, path):
        with self.root.canvas.before:
            self.bg = Rectangle(source=path, pos=self.root.pos, size=Window.size)
        self.root.bind(size=self.update_bg)

    def update_bg(self, instance, value):
        self.bg.size = Window.size

    def play_video(self, path):
        try:
            subprocess.Popen(['start', path], shell=True)  # Windows
        except Exception as e:
            print(f"Ошибка: {e}")

    def on_key_down(self, window, key, *args):
        if key == 27:  # Escape
            App.get_running_app().stop()

if __name__ == '__main__':
    MainApp().run()
