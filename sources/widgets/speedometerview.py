from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.animation import Animation

speedometerview_layout = '''
<SpeedometerView@FloatLayout>:
    canvas:
        # Background
        Rectangle:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView.png'
            pos:
                self.pos[0] + (self.width - min(self.size)) / 2.0,\
                self.pos[1] + (self.height - min(self.size)) / 2.0
        
        # Straight line
        Rectangle:
            size: \
                (min(self.size) / 2.0 * (self.value - self.ang_value_max)/(self.lin_value_max - self.ang_value_max), min(self.size)) \
                if self.value > self.ang_value_max else \
                (0, 0)
            pos: \
                self.pos[0] + self.width / 2.0, \
                self.pos[1] + 1.0
            source: 'images/SpeedView_SpeedBlur2.png'
        
        # Arc line
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_SpeedBlur.png'
            pos: 
                self.pos[0] + (self.width - min(self.size)) / 2,\
                self.pos[1] + (self.height - min(self.size)) / 2
            angle_start: self.ang_start
            angle_end: self.ang_start + self.ang_wide * self.value / self.ang_value_max
        
        # Arrow
        PushMatrix
        Rotate:
            angle: \
                -self.ang_start - self.ang_wide * self.max / self.ang_value_max \
                if self.max < self.ang_value_max else 0
            origin: self.center
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_Arrow.png'
            pos:
                self.pos[0] + (self.width - min(self.size)) / 2 \
                if self.max < self.ang_value_max else \
                self.pos[0] + (self.width - min(self.size)) / 2 + \
                (self.width / 2 - (self.width - min(self.size)) / 2) * \
                (self.max - self.ang_value_max)/(self.lin_value_max - self.ang_value_max),\
                self.pos[1] + (self.height - min(self.size)) / 2
        PopMatrix
        
    Label:
        text: str(int(root.value))
        pos: root.pos[0], root.pos[1] + self.height * 0.05
        size_hint: (None, None)
        font_size: min(root.size) / 3.5
        font_name: 'fonts/SysBoldItalic.ttf'
        markup: True
        size: root.size
        
        ### DEBUG ONLY ###
        # canvas:       
            # Color:
            #     rgba: 1,0,0,0.1
            # Rectangle
            #     size: self.size
            #     pos: self.pos
        
'''
Builder.load_string(speedometerview_layout)


class SpeedometerView(FloatLayout):
    ang_value_max = 120.0
    ang_start = -135.0
    ang_end = 0.0
    ang_wide = abs(ang_end - ang_start)

    lin_value_max = 182.0

    max = NumericProperty(0.0)
    value = NumericProperty(0.0)

    anim = None

    def set_speed_value(self, value):
        self.anim = Animation(value=value, max=max(self.max, value), d=0.2)
        self.anim.start(self)
        # self.sp_val = value
        # self.sp_max = max(value, self.sp_max)

    def reset_max_speed(self):
        self.max = 0.0

    def __init__(self, **kwargs):
        super(SpeedometerView, self).__init__(**kwargs)



