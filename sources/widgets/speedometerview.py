from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

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
                (min(self.size) / 2.0 * (self.sp_val - self.sp_ang_val_max)/(self.sp_lin_val_max - self.sp_ang_val_max), min(self.size)) \
                if self.sp_val > self.sp_ang_val_max else \
                (0, 0)
            pos: \
                self.pos[0] + (self.width - min(self.size)) / 2.0 + self.width / 2.0, \
                self.pos[1] + (self.height - min(self.size)) / 2.0 + 0.5
            source: 'images/SpeedView_SpeedBlur2.png'
        
        # Arc line
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_SpeedBlur.png'
            pos: 
                self.pos[0] + (self.width - min(self.size)) / 2,\
                self.pos[1] + (self.height - min(self.size)) / 2
            angle_start: self.sp_ang_start
            angle_end: self.sp_ang_start + self.sp_ang_wide * self.sp_val / self.sp_ang_val_max
        
        # Arrow
        PushMatrix
        Rotate:
            angle: \
                -self.sp_ang_start - self.sp_ang_wide * self.sp_max / self.sp_ang_val_max \
                if self.sp_max < self.sp_ang_val_max else 0
            origin: self.center
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_Arrow.png'
            pos:
                self.pos[0] + (self.width - min(self.size)) / 2 \
                if self.sp_max < self.sp_ang_val_max else \
                self.pos[0] + (self.width - min(self.size)) / 2 + \
                self.width / 2 * (self.sp_max - self.sp_ang_val_max)/(self.sp_lin_val_max - self.sp_ang_val_max),\
                self.pos[1] + (self.height - min(self.size)) / 2
        PopMatrix
        
    Label:
        text: str(int(root.sp_val))
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
    sp_ang_val_max = 120.0
    sp_ang_start = -135.0
    sp_ang_end = 0.0
    sp_ang_wide = sp_ang_end - sp_ang_start

    sp_lin_val_max = 182.0

    sp_max = NumericProperty(0.0)
    sp_val = NumericProperty(0.0)

    def set_speed_value(self, value):
        self.sp_val = value
        self.sp_max = max(value, self.sp_max)

    def __init__(self, **kwargs):
        super(SpeedometerView, self).__init__(**kwargs)



