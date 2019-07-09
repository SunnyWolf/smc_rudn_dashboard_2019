from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.animation import Animation

turnlight_layout = '''
<IndicatorLight>:
    direction: 'left'
    source: 'images/TurnLight_Left.png' if root.direction == 'left' else 'images/TurnLight_Right.png'
'''

Builder.load_string(turnlight_layout)


class TurnLight(Image):
    def __init__(self, **kwargs):
        super(TurnLight, self).__init__(**kwargs)

        self.anim = Animation(opacity=1.0, d=0.5) + Animation(opacity=0.0, d=0.5)
        self.anim.repeat = True

    def on(self, value):
        self.anim.start()

    def off(self):
        self.anim.stop()
        self.opacity = 0.0

