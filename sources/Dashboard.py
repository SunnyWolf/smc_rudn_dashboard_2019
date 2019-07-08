from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.lang import Builder

dashboard_layout = '''
#:import SpeedometerView sources.widgets.speedometerview
#:import CurrentView sources.widgets.currentview
#:import IndicatorLight sources.widgets.indicatorlight
#:import ModeView sources.widgets.modeview

<Dashboard>
    BoxLayout:
        orientation: 'vertical'
        # Slider:
        #     id: sl1
        #     size_hint: 1., 0.1
        #     max: 160
        #     min: 0
        # Slider:
        #     id: sl2
        #     size_hint: 1., 0.1
        #     max: 60
        #     min: -120
        FloatLayout:
            BoxLayout
                orientation: 'horizontal'
                SpeedometerView:
                    id: speed
                CurrentView:
                    id: current
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 0.2, 0.6
                    ModeView:
                        id: mode
                    IndicatorLight:
                        id: light
'''
Builder.load_string(dashboard_layout)


# Main screen
class Dashboard(BoxLayout):
    def test(self, obj):
        self.ids.light.value = not self.ids.light.value
        pass

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

