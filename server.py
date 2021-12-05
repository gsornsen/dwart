from MicroWebSrv2.microWebSrv2 import MicroWebSrv2
from time import sleep

class WebServer:
    def __init__(self):
        self.server = MicroWebSrv2()
        self.start_web_server()

    def start_web_server(self):
        self.server.SetEmbeddedConfig()
        self.server._slotsCount = 4 # ESP32 OOM if opening too many sockets
        self.server.NotFoundURL = "/" # Redirect to home on 404
        print("Starting Web Server!")
        self.server.StartManaged()
        self.run_server()

    def run_server(self):
        while self.server.IsRunning:
            sleep(0.001)

    def stop_server(self):
        print("Stopping Server!")
        self.server.Stop()
