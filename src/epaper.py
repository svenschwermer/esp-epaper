import wifi
from epd import epd
import time
import urequests
import json
import font
from framebuf import FrameBuffer, MONO_VMSB

key_id = 'bm672hb24te000b24thg'
with open('key_secret', 'rt') as f:
    key_secret = f.read()
project_id = 'bg5tq3e4go0ecm2di8j0'
sensor_id = 'bhnc8g9qitfg008o375g'
#sensor_id = 'emuc0ujldhqdqebrvv2b6dg'

def encode_basic_auth(username, password):
    import ubinascii
    formated = b"{}:{}".format(username, password)
    formated = ubinascii.b2a_base64(formated)[:-1].decode("ascii")
    return {'Authorization' : 'Basic {}'.format(formated)}

def large_centered_text(fb, s, avail_width, y):
    x = (avail_width - font.str_width(s)) // 2
    for c in s:
        ch, width = font.get_ch(c)
        chfb = FrameBuffer(bytearray(ch), width, font.height, MONO_VMSB)
        fb.blit(chfb, x, y)
        x += width

e = epd()
e.display_text('Connecting to WiFi...')
wifi.connect()
state_url = 'https://api.disruptive-technologies.com/v2/projects/{}/devices/{}'.format(project_id, sensor_id)
auth_header = encode_basic_auth(key_id, key_secret)
large_y = (e.e.height - 8 - font.height) // 2

last = [None, None, None]
while True:
    resp = urequests.get(state_url, headers=auth_header)
    resp_json = json.loads(resp.text)

    t = resp_json['reported']['temperature']['updateTime']
    new = [
        '{:.1f}°C'.format(resp_json['reported']['temperature']['value']),
        resp_json['labels']['name'],
        '{} {}'.format(t[:10], t[11:19]),
    ]

    if new != last:
        with e as fb:
            large_centered_text(fb, new[0], e.e.width, large_y)
            fb.text(new[1], 0, 120, 0)
            fb.text(new[2], 296-8*len(new[2]), 120, 0)
        last = new

    time.sleep(3)
