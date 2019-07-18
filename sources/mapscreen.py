from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

mapscreen_layout = '''
<MapScreen>:
    BoxLayout:
        orientation: 'vertical'
        id: layout
        Button:
            size_hint: 1.0, 0.1
            font_size: 30
            text: 'DASHBOARD'
            on_release: app.root.current = 'main'
'''


class MapScreen(Screen):
    def __init__(self, **kw):
        super(MapScreen, self).__init__(**kw)


Builder.load_string(mapscreen_layout)
