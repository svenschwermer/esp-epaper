from machine import Pin, SPI
import framebuf
import epaper2in9

class epd:
    def __init__(self):
        self.spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
        self.e = epaper2in9.EPD(self.spi, cs=Pin(5), dc=Pin(19), rst=Pin(12), busy=Pin(4))
        self.e.init()

        self.buf = bytearray(self.e.width * self.e.height // 8)
        self.fb = framebuf.FrameBuffer(self.buf, self.e.width, self.e.height, framebuf.MONO_VMSB)

    def __enter__(self):
        self.fb.fill(1)
        return self.fb

    def __exit__(self, exc_type, exc, exc_tb):
        self.e.set_frame_memory(self.buf, 0, 0, self.e.width, self.e.height)
        self.e.display_frame()

    def display_text(self, s, x=0, y=0):
        self.fb.fill(1)
        self.fb.text(s, x, y, 0)
        self.e.set_frame_memory(self.buf, 0, 0, self.e.width, self.e.height)
        self.e.display_frame()
