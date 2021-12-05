from MicroWebSrv2.webRoute import WebRoute, GET
from server import WebServer
from led_driver import LEDDriver


driver = LEDDriver()


@WebRoute(GET, "/test")
def test(microWebSrv2, request):
    request.Response.ReturnOk("I'm alive!\n")

@WebRoute(GET, "/rain")
def rain(microWebSrv2, request):
    request.Response.ReturnOk("Making it rain!\n")
    driver.rain()

@WebRoute(GET, "/rainbow")
def rainbow(microWebSrv2, request):
    request.Response.ReturnOk("Making it rainbow!\n")
    driver.rainbow()

@WebRoute(GET, "/pause")
def pausing(microWebSrv2, request):
    request.Response.ReturnOk("Pausing!\n")
    driver.pause()

@WebRoute(GET, "/turn_off_leds")
def turn_off_leds(microWebSrv2, request):
    request.Response.ReturnOk("Turning off LEDs!\n")
    driver.led_off_handler()


server = WebServer()
