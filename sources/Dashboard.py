from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


# основной экран
class Dashboard(FloatLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.background = Image(source="../images.png")
        self.add_widget(self.background)
