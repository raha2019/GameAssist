#from gtts import gTTs
import pyttsx3
#import pyscreenshot as ImageGrab
from PIL import ImageGrab
import cv2
import numpy as np
import image_slicer
from playsound import playsound
import time

def order66(backgroundImage):
    firstluckbox1(backgroundImage)
    firstluckbox2(backgroundImage)
    firstluckbox3(backgroundImage)
    firstpoop1(backgroundImage)
    firstpoop2(backgroundImage)
    # firstpipe(backgroundImage)

def firstluckbox1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox1.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box Top Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox1.png',img_rgb)

def firstluckbox2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box Top Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox2.png',img_rgb)

def firstluckbox3(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox3.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box Top Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox3.png',img_rgb)

def firstpoop1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('poop1.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Top Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop1.png',img_rgb)

def firstpoop2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('poop2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Top Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop2.png',img_rgb)

# def firstpipe(backgroundImage):
#     engine = pyttsx3.init()
#     backgroundImage = 'REEE_01_01.png'
#     img_rgb = cv2.imread(backgroundImage)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread('pipe.png',0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#     threshold = 0.3
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#         engine.say("There is a pipe on Top Left of the playing field")
#         engine.runAndWait()
#     cv2.imwrite('resultpipe.png',img_rgb)


def order69(backgroundImage):
    backgroundImage = 'REEE_01_02.png'
    secondluckbox1(backgroundImage)
    secondluckbox2(backgroundImage)
    secondluckbox3(backgroundImage)
    secondpoop1(backgroundImage)
    secondpoop2(backgroundImage)
    # secondpipe(backgroundImage)

def secondluckbox1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox1.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Top Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox1.png',img_rgb)

def secondluckbox2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Top Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox2.png',img_rgb)

def secondluckbox3(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox3.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Top Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox3.png',img_rgb)

def secondpoop1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('poop1.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Top Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop1.png',img_rgb)

def secondpoop2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_01_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('poop2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Top Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop2.png',img_rgb)

# def secondpipe(backgroundImage):
#     engine = pyttsx3.init()
#     backgroundImage = 'REEE_01_02.png'
#     img_rgb = cv2.imread(backgroundImage)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread('pipe.png',0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#     threshold = 0.3
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#         engine.say("There is a pipe on Top Right of the playing field")
#         engine.runAndWait()
#     cv2.imwrite('resultpipe.png',img_rgb)

def order420(backgroundImage):
    # backgroundImage = "PipeTest.png"
    backgroundImage = 'REEE_02_01.png'
    thirdluckbox1(backgroundImage)
    thirdluckbox2(backgroundImage)
    thirdluckbox3(backgroundImage)
    thirdpoop1(backgroundImage)
    thirdpoop2(backgroundImage)
    # thirdpipe(backgroundImage)

def thirdluckbox1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox1.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a luckybox on Bottom Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox1.png',img_rgb)

def thirdluckbox2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a luckybox on Bottom Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox2.png',img_rgb)

def thirdluckbox3(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox3.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a luckybox on Bottom Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox3.png',img_rgb)

def thirdpoop1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('poop1.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Bottom Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop1.png',img_rgb)

def thirdpoop2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_01.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('poop2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Bottom Left of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop2.png',img_rgb)

# def thirdpipe(backgroundImage):
#     engine = pyttsx3.init()
#     backgroundImage = 'REEE_02_01.png'
#     img_rgb = cv2.imread(backgroundImage)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread('pipe.png',0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#     threshold = 0.3
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#         engine.say("There is a pipe on Bottom Left of the playing field")
#         engine.runAndWait()
#     cv2.imwrite('resultpipe.png',img_rgb)

def order69420(backgroundImage):
    # backgroundImage = "PipeTest.png"
    backgroundImage = 'REEE_02_02.png'
    fourthluckbox1(backgroundImage)
    fourthluckbox2(backgroundImage)
    fourthluckbox3(backgroundImage)
    fourthpoop1(backgroundImage)
    fourthpoop2(backgroundImage)
    # fourthpipe(backgroundImage)

def fourthluckbox1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox1.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Bottom Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox1.png',img_rgb)

def fourthluckbox2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Bottom Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox2.png',img_rgb)

def fourthluckbox3(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('luckybox3.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a lucky box on Bottom Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultluckbox3.png',img_rgb)

def fourthpoop1(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('poop1.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Bottom Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop1.png',img_rgb)

def fourthpoop2(backgroundImage):
    engine = pyttsx3.init()
    backgroundImage = 'REEE_02_02.png'
    img_rgb = cv2.imread(backgroundImage)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('poop2.png',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.45
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        engine.say("There is a goomba on Bottom Right of the playing field")
        engine.runAndWait()
    cv2.imwrite('resultpoop2.png',img_rgb)

# def fourthpipe(backgroundImage):
#     engine = pyttsx3.init()
#     backgroundImage = 'REEE_02_02.png'
#     img_rgb = cv2.imread(backgroundImage)
#     img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     template = cv2.imread('pipe.png',0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#     threshold = 0.3
#     loc = np.where( res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
#         engine.say("There is a pipe on Bottom Right of the playing field")
#         engine.runAndWait()
#     cv2.imwrite('resultpipe.png',img_rgb)

while True:
    engine = pyttsx3.init()
    time.sleep(3)
    im = ImageGrab.grab()
    im.save('REEE.png')
    image_slicer.slice('REEE.png', 4)
    backgroundImage = "REEE_01_01.png"
    order66(backgroundImage)
    backgroundImage = "REEE_01_02.png"
    order69(backgroundImage)
    backgroundImage = "REEE_02_01.png"
    order66(backgroundImage)
    backgroundImage = "REEE_02_02.png"
    order69420(backgroundImage)
