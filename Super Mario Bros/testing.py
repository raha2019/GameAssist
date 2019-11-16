import cv2
import numpy as np
import image_slicer


image_slicer.slice('TestOne.png', 4)

TopLeft = 'REE_01_01.png'
TopRight = 'REE_01_02.png'
BottomLeft = 'REE_01_03.png'
BottomRight = 'REE_01_04.png'

img_rgb = cv2.imread("TestOne_02_01.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('copy.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.45
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imwrite('testingagain.png',img_rgb)
#lol
=======
cv2.imwrite('testingagainagain.png',img_rgb)
>>>>>>> f9a86dacdf35a638c7fd81bb0064f368ef6af761
