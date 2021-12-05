import _thread as thread
from machine import Pin
from neopixel import NeoPixel
from time import sleep


DELAY = 100
DELAY_MS = DELAY / 1000
OCEAN_EYES = (0, 166, 142)
OFF = (0, 0, 0)
NUM_LEDS = 8
DIO_PIN = 15


class LEDDriver():
    def __init__(self, num_leds=NUM_LEDS, dio_pin=DIO_PIN):
        self.num_leds = num_leds
        self.dio_pin = dio_pin
        self.pin = Pin(self.dio_pin, Pin.OUT)
        self.np = NeoPixel(self.pin, self.num_leds)
        self.animate = False

    def toggle_animation_state(self):
        if self.animate:
            self.animate = False

    def wheel(self, position):
        if position < 0 or position > 255:
            return (0, 0, 0)
        if position < 85:
            return (255 - position * 3, position * 3, 0)
        if position < 170:
            position -= 85
            return (0, 255 - position * 3, position * 3)
        position -= 170
        return (position * 3, 0, 255 - position * 3)

    def rainbow(self):
        self.toggle_animation_state()
        thread.start_new_thread(self.rainbow_handler, ())
        thread.exit()

    def rainbow_handler(self):
        self.animate = True
        while self.animate:
            for j in range(255):
                for i in range(self.num_leds):
                    rc_index = (i * 256 // self.num_leds) + j
                    self.np[i] = self.wheel(rc_index & 255)
                self.np.write()
                sleep(0.0001)

    def rain(self):
        self.toggle_animation_state()
        thread.start_new_thread(self.rain_handler, ())
        thread.exit()

    def rain_handler(self):
        self.animate = True
        while self.animate:
            for led in range(self.num_leds):
                self.np[led] = OCEAN_EYES
                self.np.write()
                sleep(DELAY_MS)
            for led in range(self.num_leds):
                self.np[led] = OFF
                self.np.write()
                sleep(DELAY_MS)
        return

    def led_off_handler(self):
        for led in range(self.num_leds):
            self.np[led] = OFF
        self.np.write()
        self.pause()

    def pause(self):
        self.animate = False
