from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.lang import Builder

dashboard_layout = '''
#:import SpeedometerView sources.widgets.speedometerview
#:import CurrentView sources.widgets.currentview
#:import IndicatorLight sources.widgets.indicatorlight
#:import ModeView sources.widgets.modeview
#:import TurnLight sources.widgets.turnlight

<Dashboard>
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
                size_hint: 1, 1
                Widget
                    size_hint: 1, 1
                ModeView:
                    id: mode
                IndicatorLight:
                    id: light
                Widget
                    size_hint: 1, 0.3

        BoxLayout
            orientation: 'horizontal'
            TurnLight:
                id: tl_left
                direction: 'left'
            Widget
            TurnLight:
                id: tl_right
                direction: 'right'
        
        Image:
            id: logo
            source: 'images/Logo_RUDN.png'
                        
'''
Builder.load_string(dashboard_layout)


# Main screen
class Dashboard(BoxLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

        self.speed = self.ids.speed
        self.current = self.ids.current
        self.light = self.ids.light
        self.tl_left = self.ids.tl_left
        self.tl_right = self.ids.tl_right

        logo = self.ids.logo
        anim = Animation(opacity=1.0, d=1) + Animation(opacity=0.0, d=1.5)
        anim.start(logo)
