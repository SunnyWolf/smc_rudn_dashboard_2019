from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

speedometerview_layout = '''
<SpeedometerView@FloatLayout>:
    canvas:
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView.png'
            pos:
                self.width / 2 + min(self.size) / 2 + (self.width - min(self.size)),\
                self.height / 2 - min(self.size) / 2
                
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_BatteryGreen.png'
            pos:
                self.width / 2 + min(self.size) / 2 + (self.width - min(self.size)),\
                self.height / 2 - min(self.size) / 2
            angle_start: -150
            angle_end: -150 - (210 - 150) * self.bt_val
            
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_BatteryRed.png' if self.bt_val < 0.20 else 'images/SpeedView_BatteryGreen.png'
            pos:
                self.width / 2 + min(self.size) / 2 + (self.width - min(self.size)),\
                self.height / 2 - min(self.size) / 2
            angle_start: -150
            angle_end: -150 - (210 - 150) * self.bt_val

        PushMatrix
        Rotate:
            axis: 0,0,1
            angle: -self.sp_ang_start - self.sp_ang_wide * self.sp_val / self.sp_val_max
            origin: self.center
        Ellipse:
            size: min(self.size), min(self.size)
            source: 'images/SpeedView_SpeedBlur.png'
            pos: 
                self.width / 2 + min(self.size) / 2 + (self.width - min(self.size)),\
                self.height / 2 - min(self.size) / 2
            angle_start: -2 - self.sp_ang_wide * self.sp_val / self.sp_val_max
            angle_end: 0
        PopMatrix
        
        ### DEBUG ONLY ###
        # Color:
        #     rgba: 1,0,0,0.1
        # Rectangle
        #     size: self.size
        #     pos: self.pos

'''
Builder.load_string(speedometerview_layout)


class SpeedometerView(FloatLayout):
    sp_val_max = 160.0
    sp_ang_start = -120.0
    sp_ang_end = 120.0
    sp_ang_wide = sp_ang_end - sp_ang_start

    sp_val = NumericProperty(0.0)
    bt_val = NumericProperty(0.0)

    def set_speed_value(self, instance, value):
        self.sp_val = value

    def set_battery_percent(self, instance, value):
        self.bt_val = value

    def __init__(self, **kwargs):
        super(SpeedometerView, self).__init__(**kwargs)



