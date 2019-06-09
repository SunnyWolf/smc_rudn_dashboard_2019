from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

currentview_layout = '''
<CurrentView@FloatLayout>:
    canvas:
        # Background
        Rectangle:
            size: min(self.size), min(self.size)
            source: 'images/CurrentView.png'
            pos:
                self.pos[0] + (self.width - min(self.size)) / 2.0,\
                self.pos[1] + (self.height - min(self.size)) / 2.0

        # Straight line
        Rectangle:
            size: \
                ((min(self.size) / 2.0 - (self.width - min(self.size)) / 2.0) * (-self.value - self.ang_o_value_max)/(self.lin_val_max - self.ang_o_value_max) - 0.2, min(self.size)) \
                if self.value < -self.ang_o_value_max else \
                (0, 0)
            pos: \
                self.center[0] - (min(self.size) / 2.0 - (self.width - min(self.size)) / 2.0) * (-self.value - self.ang_o_value_max)/(self.lin_val_max - self.ang_o_value_max), \
                self.pos[1] + (self.height - min(self.size)) / 2.0
            #     self.pos[0] + (self.width - min(self.size)) / 2.0, \
            #     self.pos[1] + (self.height - min(self.size)) / 2.0
            source: 'images/CurrentView_Orange2.png'

        # Arc line
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/CurrentView_Green.png' if self.value > 0 else 'images/CurrentView_Orange1.png'
            pos: 
                self.pos[0] + (self.width - min(self.size)) / 2,\
                self.pos[1] + (self.height - min(self.size)) / 2
            angle_start: \
                self.ang_start
            angle_end: \
                self.ang_start + self.ang_g_wide * self.value / self.ang_g_value_max \
                if self.value > 0 else \
                self.ang_start + self.ang_o_wide * self.value / self.ang_o_value_max
    Label:
        text: str(int(root.value))
        pos: root.pos[0], root.pos[1] + self.height * 0.05
        size_hint: (None, None)
        font_size: min(root.size) / 3.5
        font_name: 'fonts/SysBoldItalic.ttf'
        markup: True
        size: root.size

'''
Builder.load_string(currentview_layout)


class CurrentView(FloatLayout):
    ang_start = 90.0

    ang_o_value_max = 80.0
    ang_o_end = 0.0
    ang_o_wide = abs(ang_o_end - ang_start)

    ang_g_value_max = 60.0
    ang_g_end = 135.0
    ang_g_wide = abs(ang_g_end - ang_start)

    lin_val_max = 138.0

    value = NumericProperty(0.0)

    anim = None

    def set_current_value(self, value):
        self.anim = Animation(value=value, d=0.2)
        self.anim.start(self)
        # self.value = value

    def __init__(self, **kwargs):
        super(CurrentView, self).__init__(**kwargs)
