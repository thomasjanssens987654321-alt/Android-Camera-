from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color

class ROISelector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_point = None
        self.rect = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.start_point = touch.pos
            with self.canvas:
                Color(1, 0, 0, .5) # Half-transparant rood
                self.rect = Rectangle(pos=touch.pos, size=(0, 0))

    def on_touch_move(self, touch):
        if self.start_point:
            # Update de grootte van de rechthoek terwijl je sleept
            self.rect.size = (touch.x - self.start_point[0], touch.y - self.start_point[1])

    def on_touch_up(self, touch):
        # Sla de definitieve coördinaten op (dit is je ROI)
        self.final_roi = (self.start_point, touch.pos)

    def confirm_selection(self):
        # De "Enter" vervanging: verwerk hier de self.final_roi met OpenCV
        print(f"ROI bevestigd: {self.final_roi}")

class MyApp(App):
    def build(self):
        return ROISelector()
