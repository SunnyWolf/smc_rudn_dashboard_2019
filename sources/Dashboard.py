from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.anchorlayout import AnchorLayout

from sources.widgets.speedometerview import SpeedometerView


# Main screen
class Dashboard(BoxLayout):
    def set_speed(self, instance, value):
        self.speed_view.set_speed_value(value)

    def set_battery(self, instance, value):
        self.speed_view.set_battery_percent(value)

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.s1 = Slider(size_hint=(1., 0.1), max=160)
        self.s2 = Slider(size_hint=(1., 0.1), max=1.0)

        self.s1.bind(value=self.set_speed)
        self.s2.bind(value=self.set_battery)

        self.al = AnchorLayout(anchor_x='center', anchor_y='center')
        self.speed_view = SpeedometerView(size_hint=(None, None), size=(400, 400))
        self.al.add_widget(self.speed_view)

        self.add_widget(self.s1)
        self.add_widget(self.s2)
        self.add_widget(self.al)

