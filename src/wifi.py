import network
from time import sleep

with open('wifi_ssid', 'rt') as f:
    wifi_ssid = f.read()
with open('wifi_key', 'rt') as f:
    wifi_key = f.read()

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.active():
        sta_if.active(True)
        while not sta_if.active():
            sleep(0.1)
    if not sta_if.isconnected():
        sta_if.connect(wifi_ssid, wifi_key)
        while not sta_if.isconnected():
            sleep(0.1)
