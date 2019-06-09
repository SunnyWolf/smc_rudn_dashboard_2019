from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.anchorlayout import AnchorLayout

from sources.widgets.speedometerview import SpeedometerView
from sources.widgets.currentview import CurrentView


# Main screen
class Dashboard(BoxLayout):
    def set_speed(self, instance, value):
        self.speed_view.set_speed_value(value)

    def set_current(self, instance, value):
        self.current_view.set_current_value(value)

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.s1 = Slider(size_hint=(1., 0.1), max=160)
        self.s2 = Slider(size_hint=(1., 0.1), min=-120, max=60, value=0)

        self.s1.bind(value=self.set_speed)
        self.s2.bind(value=self.set_current)

        self.bl = BoxLayout(orientation="horizontal")
        self.speed_view = SpeedometerView()
        self.current_view = CurrentView()
        self.bl.add_widget(self.speed_view)
        self.bl.add_widget(self.current_view)

        self.add_widget(self.s1)
        self.add_widget(self.s2)
        self.add_widget(self.bl)

