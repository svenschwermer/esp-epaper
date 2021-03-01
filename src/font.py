# micropython-font-to-py/hybrid.py /usr/share/fonts/noto/NotoSans-Medium.ttf 64 0123456789.-°C src/font
_char_set = {'?': (0, 304, 38), '-': (304, 528, 28), '.': (528, 712, 23), '0': (712, 1104, 49), '1': (1104, 1496, 49), '2': (1496, 1888, 49), '3': (1888, 2280, 49), '4': (2280, 2672, 49), '5': (2672, 3064, 49), '6': (3064, 3456, 49), '7': (3456, 3848, 49), '8': (3848, 4240, 49), '9': (4240, 4632, 49), 'C': (4632, 5064, 54), '°': (5064, 5360, 37)}

height = 63

with open("font.bin", "rb") as f:
    _font_bin = f.read()

def get_ch(ch):
    c = _char_set.get(ch, _char_set["?"])
    return (_font_bin[c[0]:c[1]], c[2])

def str_width(s):
    w = 0
    for c in s:
        w += _char_set.get(c, _char_set["?"])[2]
    return w
