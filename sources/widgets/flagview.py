from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, StringProperty, BooleanProperty

from math import sin, cos, pi

flagview_layout = '''
<FlagView>:
    name: ''
    text: ''
    description: ''
    value: False
    
    RoundedBox:
        size: root.size
        pos: root.pos
        corners: 20, 20, 20, 20
        padding: 10
        line_width: 3
    BoxLayout:
        orientation: 'vertical'
        Label:
            font_size: 20
            text: root.name
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
            close: True
        # Mesh:
        #     vertices: self.vertices
        #     indices: self.indices
'''


class FlagView(AnchorLayout):
    anchor_x = 'center'
    anchor_y = 'center'

    name = StringProperty('')
    text = StringProperty('')
    description = StringProperty('')
    value = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(FlagView, self).__init__(**kwargs)


class RoundedBox(Widget):
    corners = ListProperty([0, 0, 0, 0])
    line_width = NumericProperty(1)
    resolution = NumericProperty(100)
    points = ListProperty([])
    padding = NumericProperty(0)
    # vertices = ListProperty([[0,0,0,0],[0,0,0,0]])
    indices = NumericProperty(0)

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
        y = self.y + self.corners[1] + self.padding
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

        x = self.x + self.corners[3] + self.padding
        y = self.top - self.corners[3] - self.padding
        while a < pi:
            a += pi / self.resolution
            self.points.extend([
                x + cos(a) * self.corners[3],
                y + sin(a) * self.corners[3]
                ])

        self.points.extend(self.points[:2])


Builder.load_string(flagview_layout)
