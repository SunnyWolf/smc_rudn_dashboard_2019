from gpiozero import Button


class Gpios:
    def on_light_on(self):
        self.indicator_light.far()

    def on_light_off(self):
        self.indicator_light.close()

    def __init__(self, dashboard):
        self.indicator_light = dashboard.ids.light

        self.b_light = Button(12)
        self.b_light.when_activated = self.on_light_on
        self.b_light.when_deactivated = self.on_light_off
