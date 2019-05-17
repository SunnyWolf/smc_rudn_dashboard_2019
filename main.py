from threading import Thread
import time
import datetime
import sys

from kivy.app import App

from sources.Dashboard import Dashboard

# os.environ['KIVY_GL_BACKEND'] = 'gl'
# os.environ['KIVY_WINDOW'] = 'egl_rpi'


# Основной класс приложения
class SMCDashboardApp(App):
    def build(self):
        # основная страница
        dashboard = Dashboard()
        return dashboard


if __name__ == "__main__":
    old_excepthook = sys.excepthook

    def app_excepthook(exctype, value, traceback):
        if exctype == KeyboardInterrupt:
            print("Exception: Keyboard interrupt received")
        else:
            old_excepthook(exctype, value, traceback)
    sys.excepthook = app_excepthook

    SMCDashboardApp().run()
