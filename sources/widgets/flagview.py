from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty

from math import sin, cos, pi

flagview_layout = '''
<FlagView>:
    text: 'test'
    canvas:
        Color:
            rgba: 1,1,1,0.2
        RoundedRectangle:
            size: root.size
            pos: root.pos
            radius: 30,
        Color:
            rgba: 1,1,1,0.3
        Line:
            width: 3
            rectangle: self.x, self.y, self.width, self.height
    Label:
        font_size: 20
        text: root.text

<RoundedBox>:
    on_pos: self.compute_points()
    on_size: self.compute_points()
    on_corners: self.compute_points()
    on_resolution: self.compute_points()
    canvas:
        Line:
            # we don't care about the arguments, pass them to get
            # binding
            points: self.points
            width: self.line_width
            #loop: True
'''


class FlagView(AnchorLayout):
    anchor_x = 'center'
    anchor_y = 'center'

    def __init__(self, **kwargs):
        super(FlagView, self).__init__(**kwargs)


class RoundedBox(Widget):
    corners = ListProperty([0, 0, 0, 0])
    line_width = NumericProperty(1)
    resolution = NumericProperty(100)
    points = ListProperty([])
    padding = NumericProperty(0)

    def compute_points(self, *args):
        self.points = []

        a = - pi

        x = self.x + self.corners[0] + self.padding
        y = self.y + self.corners[0] + self.padding
        while a < - pi / 2.:
            a += pi / self.resolution
            self.points.extend([
                x + cos(a) * self.corners[0],
                y + sin(a) * self.corners[0]
                ])

        x = self.right - self.corners[1] - self.padding
        y = self.y + self.corners[1] - self.padding
        while a < 0:
            a += pi / self.resolution
            self.points.extend([
                x + cos(a) * self.corners[1],
                y + sin(a) * self.corners[1]
                ])

        x = self.right - self.corners[2] - self.padding
        y = self.top - self.corners[2] - self.padding
        while a < pi / 2.:
            a += pi / self.resolution
            self.points.extend([
                x + cos(a) * self.corners[2],
                y + sin(a) * self.corners[2]
                ])

        x = self.x + self.corners[3] - self.padding
        y = self.top - self.corners[3] - self.padding
        while a < pi:
            a += pi / self.resolution
            self.points.extend([
                x + cos(a) * self.corners[3],
                y + sin(a) * self.corners[3]
                ])

        self.points.extend(self.points[:2])


Builder.load_string(flagview_layout)
