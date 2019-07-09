from gpiozero import Button
from gpiozero import PWMOutputDevice

from widgets.indicatorlight import IndicatorLight


class Gpios:
    def on_light_side(self):
        self.indicator_light.set(IndicatorLight.SIDE)

    def on_light_close(self):
        if self.b_light_far.value is not True:
            self.indicator_light.set(IndicatorLight.CLOSE)

    def on_light_far(self):
        self.indicator_light.set(IndicatorLight.FAR)

    def on_light_off(self):
        self.indicator_light.set(IndicatorLight.OFF)

    def on_changing(self):
        if self.b_light_side.value == 1:
            if self.b_light_far.value == 1:
                self.on_light_far()
            elif self.b_light_close.value == 1:
                self.on_light_close()
            else:
                self.on_light_side()
        else:
            self.on_light_off()

    def __init__(self, dashboard):
        self.indicator_light = dashboard.ids.light

        self.b_light_side = Button(26, pull_up=None, active_state=True, bounce_time=0.1)
        self.b_light_side.when_pressed = self.on_changing
        self.b_light_side.when_released = self.on_changing

        self.b_light_close = Button(12, pull_up=None, active_state=True, bounce_time=0.1)
        self.b_light_close.when_activated = self.on_changing
        self.b_light_close.when_released = self.on_changing

        self.b_light_far = Button(16, pull_up=None, active_state=True, bounce_time=0.1)
        self.b_light_far.when_activated = self.on_changing
        self.b_light_far.when_released = self.on_changing

        # self.fan = PWMOutputDevice()
