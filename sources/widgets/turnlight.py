from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.animation import Animation

turnlight_layout = '''
<TurnLight>
    canvas:
    direction: 'left'
    source: 'images/TurnLight_Left.png' if root.direction == 'left' else 'images/TurnLight_Right.png'
    opacity: 0.0
'''

Builder.load_string(turnlight_layout)


class TurnLight(Image):
    def __init__(self, **kwargs):
        super(TurnLight, self).__init__(**kwargs)

        self.anim = Animation(opacity=1.0, d=0.5) + Animation(opacity=0.0, d=0.5)
        self.anim.repeat = True

    def on(self):
        self.anim.start(self)

    def off(self):
        self.anim.stop(self)
        self.opacity = 0.0

