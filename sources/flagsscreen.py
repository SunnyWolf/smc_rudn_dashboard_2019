from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from sources.widgets.flagview import RoundedBox

flagscreen_layout = '''
<FlagsScreen>:
    BoxLayout:
        orientation: 'vertical'
        id: layout
        Button:
            size_hint: 1.0, 0.1
            font_size: 30
            text: 'DASHBOARD'
            on_release: app.root.current = 'main'
        GridLayout:
            id: grid
            cols: 8 
'''

Builder.load_string(flagscreen_layout)


class FlagsScreen(Screen):
    def __init__(self, **kw):
        super(FlagsScreen, self).__init__(**kw)

        for i in range(24):
            self.ids.grid.add_widget(RoundedBox(corners=[20, 20, 20, 20], line_width=5, padding=5))
