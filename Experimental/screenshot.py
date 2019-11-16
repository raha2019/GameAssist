from PIL import ImageGrab
from datetime import datetime

while True:
    im = ImageGrab.grab()
    dt = datetime.now()
    fname = "pic_{}.{}.png".format(dt.strftime("%H%M_%S"), dt.microsecond // 100000)
    im.save(fname, 'png') 
