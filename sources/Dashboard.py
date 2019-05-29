from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from sources.widgets.speedometerview import SpeedometerView


# Main screen
class Dashboard(BoxLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.orientation = 'horizontal'

        self.add_widget(Widget())

        self.speed_view = SpeedometerView()
        self.add_widget(self.speed_view)

        self.add_widget(Widget())
