from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

Builder.load_file("sources/widgets/SpeedView/SpeedView.kv")


class SpeedView(FloatLayout):
    color_blue = ListProperty(
        [0.1, 0.1, 0.1])
    color_ellipse_static = ListProperty(
        [0.5, 0.5, 0.5, 1])
    color_ellipse = ListProperty(
        [0.2, 0.9, 0.2, 1])
    pass

