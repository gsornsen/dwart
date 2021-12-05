import uasyncio
from machine import Pin
from neopixel import NeoPixel
from time import sleep
from MicroWebSrv2.microWebSrv2 import MicroWebSrv2
from MicroWebSrv2.webRoute import WebRoute, GET


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


    @WebRoute(GET, "/test")
    def test(self, request):
        request.Response.ReturnOk("I'm alive!\n")

    def start_web_server(self):
        self.server = MicroWebSrv2()
        self.server.SetEmbeddedConfig()
        self.server._slotsCount = 4 # ESP32 OOM if opening too many sockets
        self.server.NotFoundURL = "/" # Redirect to home on 404
        print("Starting Web Server!")
        self.server.StartManaged()
        self.run_server()

    def run_server(self):
        while self.server.IsRunning:
            uasyncio.sleep_ms(DELAY)

    def stop_server(self):
        print("Stopping Server!")
        self.server.Stop()


driver = LEDDriver()
driver.start_web_server()
    