from kivy.lang import Builder
from kivy.uix.image import Image

indicatorlight_layout = '''
<IndicatorLight>:
    value: False
    source: 'images/Light_Close.png' if root.value == False else 'images/Light_Far.png'
'''

Builder.load_string(indicatorlight_layout)


class IndicatorLight(Image):
    def __init__(self, **kwargs):
        super(IndicatorLight, self).__init__(**kwargs)

    def far(self):
        self.value = True

    def close(self):
        self.value = False
