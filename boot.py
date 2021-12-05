import network
import json

def get_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config

def do_connect(config):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(config['ssid'], config['pass'])
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())

config = get_config()
do_connect(config)
