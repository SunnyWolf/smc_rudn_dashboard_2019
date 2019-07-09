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

    def turn_alarm(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def turn_off(self):
        self.tl_left.off()
        self.tl_right.off()
        pass

    def on_turn_light(self):
        self.turn_off()
        if self.b_turn_left.value == 1:
            self.tl_left.on()
        if self.b_turn_right.value == 1:
            self.tl_right.on()

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
        self.tl_left = dashboard.ids.tl_left
        self.tl_right = dashboard.ids.tl_right

        self.b_light_side = Button(26, pull_up=None, active_state=True)
        self.b_light_side.when_pressed = self.on_changing
        self.b_light_side.when_released = self.on_changing

        self.b_light_close = Button(12, pull_up=None, active_state=True)
        self.b_light_close.when_activated = self.on_changing
        self.b_light_close.when_released = self.on_changing

        self.b_light_far = Button(16, pull_up=None, active_state=True)
        self.b_light_far.when_activated = self.on_changing
        self.b_light_far.when_released = self.on_changing

        self.b_turn_left = Button(19, pull_up=None, active_state=True)
        self.b_turn_left.when_pressed = self.on_turn_light
        self.b_turn_left.when_released = self.on_turn_light

        self.b_turn_right = Button(20, pull_up=None, active_state=True)
        self.b_turn_right.when_pressed = self.on_turn_light
        self.b_turn_right.when_released = self.on_turn_light
        # self.fan = PWMOutputDevice()
