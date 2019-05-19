from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from sources.widgets.SpeedView.SpeedView import SpeedView


# основной экран
class Dashboard(FloatLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.background = Image(source="images/bg.png")
        self.add_widget(self.background)

        self.speed_view = SpeedView()
        self.add_widget(self.speed_view)
